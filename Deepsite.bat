@echo off
set /p PROMPT=🔥 Enter your prompt:
llama-cli.exe -m deepseek-coder-6.7b-instruct.Q4_K_M.gguf -c 2048 -n -1 --temp 0.7 --repeat_penalty 1.1 -p "%PROMPT%"
pause