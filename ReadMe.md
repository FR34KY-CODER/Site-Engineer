# Site Engineer

This project is a full-stack, locally-run web application that uses a large language model (LLM) to generate complete, self-contained websites from a single text prompt. The entire system runs on local hardware, leveraging `llama.cpp` for efficient model inference on a consumer GPU.

![Project Screenshot](https://github.com/FR34KY-CODER/WebSite-Generator/blob/main/Site%20Engineer%20Screenshot.png?raw=true)

## Features

-   **Full-Stack Application:** A complete end-to-end system with a Python FastAPI backend and a vanilla JavaScript frontend.
-   **Local LLM Inference:** Runs the DeepSeek Coder 6.7B model locally using `llama-cli.exe`, ensuring privacy and zero API costs.
-   **Real-time Streaming:** Streams the generated HTML code token-by-token, providing a live-updating editor and preview.
-   **GPU Accelerated:** Optimized to use GPU offloading (`--n-gpu-layers`) for significantly faster performance on consumer hardware.
-   **Advanced Prompt Engineering:** Utilizes a highly-structured prompt to guide the LLM into generating clean, responsive, and high-quality HTML, CSS, and JavaScript code.

## Setup and Installation

Follow these steps to get the project running on your local machine (Windows).

### 1. Clone the Repository

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
```

### 2. Install Dependencies

Ensure you have Python 3.7+ installed. Then, install the required libraries using pip:

```bash
pip install -r requirements.txt
```

### 3. Download the Model

This project requires the **DeepSeek Coder 6.7B Instruct (Q4_K_M)** model. Due to its large size, the model is not included in this repository.

-   **Create the `models` directory:**
    ```bash
    mkdir models
    ```
-   **Download the model file here:**
    [**deepseek-coder-6.7b-instruct.Q4_K_M.gguf**](https://huggingface.co/TheBloke/deepseek-coder-6.7b-instruct-GGUF/resolve/main/deepseek-coder-6.7b-instruct.Q4_K_M.gguf?download=true)
-   **Place the downloaded `.gguf` file** inside the `models` directory you just created.

### 4. Get `llama-cli.exe`

You need a compiled version of `llama-cli.exe` from the [llama.cpp](https://github.com/ggerganov/llama.cpp) project.
-   Download or compile `llama-cli.exe`.
-   Place the executable file in the root directory of this project.

### 5. Run the Application

Once the model and executable are in place, you can start the server:

```bash
python main.py
```

Your web browser should automatically open to `http://127.0.0.1:11434`, and you can start generating websites!
