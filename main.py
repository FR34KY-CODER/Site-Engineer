import asyncio
import os
import subprocess
import webbrowser
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse, Response
from pydantic import BaseModel

# --- Path Configuration ---
BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"
MODELS_DIR = BASE_DIR / "models"
LLAMA_CLI_PATH = BASE_DIR / "llama-cli.exe"

# --- Performance Configuration ---
N_GPU_LAYERS = 18 

# --- Sanity Checks ---
if not STATIC_DIR.exists() or not (STATIC_DIR / "index.html").exists():
    print(f"❌ Error: The 'static' directory or 'static/index.html' was not found.")
    print(f"Please make sure the 'static' folder is in the same directory as this script: {BASE_DIR}")
    exit()
if not LLAMA_CLI_PATH.exists():
    print(f"⚠️ Warning: '{LLAMA_CLI_PATH.name}' not found. The API will not work.")
if not MODELS_DIR.exists():
    MODELS_DIR.mkdir(exist_ok=True)

# --- Find Model ---
try:
    MODEL_FILE = next(MODELS_DIR.glob("*.gguf"))
    print(f"✅ Model found: {MODEL_FILE.name}")
    print(f"🚀 GPU Layers to offload: {N_GPU_LAYERS}")
except StopIteration:
    print(f"❌ No model file found in '{MODELS_DIR}'. Place a .gguf file there.")
    MODEL_FILE = None

# --- FastAPI App Initialization ---
app = FastAPI()

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Model for API Request ---
class GenerateRequest(BaseModel):
    prompt: str

# --- Favicon Handler ---
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return Response(status_code=204)

# --- API Endpoint for Generation (Updated with robust streaming) ---
@app.post("/api/generate")
async def generate(request: GenerateRequest):
    if not LLAMA_CLI_PATH.exists():
        async def error_stream():
            yield f"data: [ERROR] 'llama-cli.exe' not found.\n\n"
        return StreamingResponse(error_stream(), media_type="text/event-stream")

    if not MODEL_FILE:
        async def error_stream():
            yield f"data: [ERROR] No model file found in '{MODELS_DIR}'.\n\n"
        return StreamingResponse(error_stream(), media_type="text/event-stream")

    website_prompt = f"""You are a machine that only generates raw HTML code.
Your task is to convert the user's request into a single, self-contained HTML file.

**CRITICAL RULES:**
- **DO NOT** write any text, explanations, or summaries.
- **DO NOT** write any notes or tell about the code.
- **DO NOT** highlight the code using '''html markdown format 
- **DO NOT** use Markdown formatting like ```html.
- Your response **MUST** be only the HTML code with integration of CSS in style tag and Javascript in Script tag.
- Your response **MUST** start with `<!DOCTYPE html>`.
- The generated code **MUST** be fully responsive and use modern CSS and JavaScript for a high-quality, interactive user experience.

**USER REQUEST:** "{request.prompt}"

**HTML CODE ONLY:**
"""

    command = [
        str(LLAMA_CLI_PATH),
        "-m", str(MODEL_FILE),
        "-p", website_prompt,
        "--n-predict", "-1", 
        "--temp", "0.4",
        "--no-display-prompt",
        "--n-gpu-layers", str(N_GPU_LAYERS)
    ]

    async def stream_output():
        process = await asyncio.create_subprocess_exec(
            *command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
        )

        queue = asyncio.Queue()
        
        # --- ROBUST TERMINATION LOGIC ---
        # This logic is now inside the producer task. It monitors the output
        # and kills the process if it sees unwanted text.
        termination_keywords = ["note:", "explanation:", "###", "```"]

        async def read_and_queue(stream, prefix, process_to_monitor):
            try:
                while process_to_monitor.returncode is None:
                    line_bytes = await stream.readline()
                    if not line_bytes:
                        break
                    
                    line = line_bytes.decode('utf-8', errors='replace').strip()

                    # # Check for termination keywords in the generated data
                    # if prefix == "[DATA]" and any(keyword in line.lower() for keyword in termination_keywords):
                    #     print(f"--- Termination keyword detected in output. Stopping generation. ---")
                    #     if process_to_monitor.returncode is None:
                    #         try:
                    #             process_to_monitor.terminate()
                    #         except ProcessLookupError:
                    #             pass # Process already gone
                    #     break

                    await queue.put(f"data: {prefix} {line}\n\n")
            finally:
                await queue.put(None)

        stdout_task = asyncio.create_task(read_and_queue(process.stdout, "[DATA]", process))
        stderr_task = asyncio.create_task(read_and_queue(process.stderr, "[STATUS]", process))

        finished_producers = 0
        while finished_producers < 2:
            item = await queue.get()
            if item is None:
                finished_producers += 1
                continue
            yield item
        
        # Clean up tasks
        stdout_task.cancel()
        stderr_task.cancel()
        await asyncio.gather(stdout_task, stderr_task, return_exceptions=True)

        if process.returncode is None:
            await process.wait()
            
        yield "data: [DONE]\n\n"

    return StreamingResponse(stream_output(), media_type="text/event-stream")


# --- Static File Serving ---
@app.get("/")
async def read_index():
    return FileResponse(STATIC_DIR / "index.html")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# --- Main Execution ---
if __name__ == "__main__":
    host = "127.0.0.1"
    port = 11434
    url = f"http://{host}:{port}"
    
    print("--- AI Website Generator ---")
    print(f"🔗 Backend running at: {url}")
    print(f"📂 Serving frontend from: {STATIC_DIR / 'index.html'}")
    
    if MODEL_FILE:
        webbrowser.open(url)
    else:
        print("\n⚠️ Server started, but you must add a model to the 'models' folder to generate websites.")

    uvicorn.run(app, host=host, port=port)
