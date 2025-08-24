# Stable Diffusion Prompt Builder Project

## Overview
Created a Python script `main.py` that reads lines from standard input until the sentinel line **THE END** is encountered.  
For each line, the script builds an accumulating description, sends a prompt to Ollama (using the Juggernaut XL v9 model, no LoRA) and outputs a set of Stable Diffusion parameters:

- Positive Stable Diffusion prompt  
- Negative Stable Diffusion prompt  
- CFG Scale  
- Optimum Image Resolution  
- Steps (up to 500)  
- Scheduler (chosen from the allowed list)

The current implementation includes a placeholder `call_ollama` function that generates deterministic dummy data; it can be replaced with a real Ollama API/CLI call.

## Files
- **main.py** – Core script implementing the described functionality (see file content in the repository).

## Task Progress
- [x] Analyze requirements
- [x] Set up necessary files
- [x] Implement main functionality
- [ ] Handle edge cases
- [ ] Test the implementation
- [ ] Verify results
