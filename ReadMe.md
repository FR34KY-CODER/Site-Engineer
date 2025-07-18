# 🚧 Site Engineer: AI-Powered Local Website Generator

Site Engineer is a **fully local full-stack web application** that transforms a simple prompt into a complete, responsive website — all with the help of a large language model running on your **own GPU**. No cloud. No API keys. No limits.

> 🧠 Powered by **DeepSeek Coder 6.7B**, streamed in real-time via `llama.cpp`.

![Site Engineer Screenshot](https://github.com/FR34KY-CODER/WebSite-Generator/blob/main/Site%20Engineer%20Screenshot.png?raw=true)

---

## ✨ Key Features

* ⚙️ **Full-Stack Application**
  Combines a **FastAPI backend** with a **vanilla JavaScript frontend** for seamless interaction.

* 💻 **Runs Fully Local**
  Uses [llama.cpp](https://github.com/ggerganov/llama.cpp)'s `llama-cli.exe` to infer LLM outputs directly on your GPU — no internet, no cost.

* ⚡ **Real-Time Streaming Output**
  Experience website generation token-by-token as code is streamed into a live editor and preview.

* 🧠 **Deep Prompt Engineering**
  Utilizes a custom-tuned system prompt that guides the LLM to produce high-quality, clean, and fully responsive HTML, CSS, and JS code.

* 🚀 **GPU Accelerated Inference**
  Support for `--n-gpu-layers` ensures you get maximum performance out of your hardware.

---

## 🖥️ Demo Preview

<p align="center">
  <img src="https://github.com/FR34KY-CODER/WebSite-Generator/blob/main/Site%20Engineer%20Screenshot.png?raw=true" alt="Site Engineer UI" width="85%">
</p>

---

## 📦 Setup and Installation

### 🔧 Requirements

* **Windows OS** (currently tested only on Windows)
* **Python 3.7+**
* **Consumer GPU with enough VRAM (6GB+)**
* Internet access (only for initial model download)

---

### 🧪 Step-by-Step Installation

#### 1. 📁 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/WebSite-Generator.git
cd WebSite-Generator
```

#### 2. 📦 Install Python Dependencies

```bash
pip install -r requirements.txt
```

#### 3. 📥 Download the Model

* Create a folder named `models`:

```bash
mkdir models
```

* Download the model file:
  [`deepseek-coder-6.7b-instruct.Q4_K_M.gguf`](https://huggingface.co/TheBloke/deepseek-coder-6.7b-instruct-GGUF/resolve/main/deepseek-coder-6.7b-instruct.Q4_K_M.gguf?download=true)

* Move it into the `models` folder.

#### 4. ⚙️ Get `llama-cli.exe`

Download or build [`llama-cli.exe`](https://github.com/ggerganov/llama.cpp) and place it in the root directory.

> 🛠️ Tip: You can compile it using `cmake` and `make` or download precompiled binaries from the community.

---

### ▶️ Run the Application

```bash
python main.py
```

Your default browser will open automatically to:

```
http://127.0.0.1:11434
```

You’re now ready to generate fully functional websites using a single text prompt!

---

## 🧠 How It Works

1. **You enter a text prompt**, like "Portfolio site for a game developer with a dark theme."
2. The prompt is sent to the **DeepSeek Coder 6.7B** model running locally via `llama-cli`.
3. The model **streams code token-by-token** through FastAPI to the browser.
4. A **live editor** updates HTML/CSS/JS in real-time — with an instant preview!

---

## 🛡️ Privacy & Cost

* ✅ No internet connection required after setup.
* ✅ No OpenAI, no HuggingFace API keys.
* ✅ 100% local. 100% free.

---

## 📚 Tech Stack

| Layer       | Tech                        |
| ----------- | --------------------------- |
| LLM Backend | DeepSeek Coder 6.7B (GGUF)  |
| Inference   | llama.cpp (`llama-cli.exe`) |
| Server      | FastAPI                     |
| Frontend    | HTML, CSS, Vanilla JS       |
| Streaming   | Server-Sent Events (SSE)    |

---

## 📸 Demo and ScreenShots

> *Coming Soon....
<p><img src="https://camo.githubusercontent.com/8adbeb4e0a139c2d1e39e9d0e54ac0ecc63390d095d15aa07ce25b51eaee408e/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f31313165626f6e4d733930594c752f67697068792e676966"></p>

---

## 📄 License

MIT License — see [`LICENSE`](LICENSE) for details.

---

## 💬 Contribute / Feedback

Got a feature idea or bug report?
Feel free to open an [Issue](https://github.com/YOUR_USERNAME/WebSite-Generator/issues) or drop a [Pull Request](https://github.com/YOUR_USERNAME/WebSite-Generator/pulls)!

---

## 🚀 Credits

Created by [FR34K](https://github.com/FR34KY-CODER) — powered by passion, code, and caffeine.
