# Stable Diffusion Prompt Builder

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

`stable_diffusion_prompt_builder` is a small Python utility that helps you iteratively construct prompts for **Stable Diffusion** using **Ollama**.  
The script can operate in two modes:

1. **Interactive mode** – type description lines one‑by‑one; the program stops when you enter a line containing exactly `THE END`.  
2. **File mode** – pass one or more text files as command‑line arguments; their contents are concatenated (newline‑separated) and sent to Ollama in a single request.

For every input (interactive line or concatenated file text) Ollama is asked to generate:

- Positive Stable Diffusion prompt  
- Negative Stable Diffusion prompt  
- CFG Scale  
- Optimum Image Resolution  
- Number of steps (up to 500)  
- Scheduler (chosen from a predefined list)

The prompt always includes the instruction **“Use proper weights for drawn elements.”** and references **model Juggernaut XL v9, no LoRA**.  
The actual CLI call uses the placeholder model `gemma3:27b` (`ollama run gemma3:27b …`). If the Ollama CLI fails, deterministic placeholder output is returned.

An optional `-o <filename>` flag lets you append the generated parameters to a file in addition to printing them to stdout.

## Features

- **Dual input modes** (interactive & file‑based)  
- Automatic **scheduler list** handling (full list of 30+ schedulers)  
- **Weight hint** (`Use proper weights for drawn elements.`) to improve prompt quality  
- **Fallback placeholder** output for environments without Ollama installed  
- Simple **output redirection** via `-o` flag  

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/chazzofalf/better_stable_diffusion_prompts
   cd stable_diffusion_prompt_builder
   ```

2. **Make sure you have Python 3.9+**  

   The script uses only the standard library, so no additional packages are required.

3. **Install Ollama** (optional, required for real model calls)

   Follow the official Ollama installation guide: https://github.com/ollama/ollama

## Usage

### Interactive mode

```bash
./main.py
```

You will see a prompt:

```
Enter lines of description (type 'THE END' on a line by itself to finish):
```

Type your description line by line. When you are done, type `THE END`. After each line the script will call Ollama (or use the placeholder) and print the generated Stable Diffusion parameters.

### File mode

```bash
./main.py description1.txt description2.txt -o output.txt
```

- All supplied files are read, concatenated with newlines, and sent as a single prompt.  
- The generated parameters are printed to the console **and** appended to `output.txt` because of the `-o` flag.

### Example

Given the example prompt in `example1.txt`:

```
I am standing on a lush grassy field.
The are seven kilometer high mountains in the far distance.
...
```

Running:

```bash
./main.py example1.txt
```

will produce something similar to:

```
--- Generated Stable Diffusion Parameters ---
Positive Prompt: placeholder positive prompt
Negative Prompt: placeholder negative prompt
CFG Scale: 7
Resolution: 512px
Steps: 50
Scheduler: DDIM
--- End --------------------------------------
```

When Ollama is available, the output will contain realistic prompts and settings based on the description.

## Scheduler List

The script supports the following schedulers (as defined in `design.txt`):

- DDIM
- DDPM
- DEIS
- DEIS Karras
- DPM++ 2S
- DPM++ 2S Karras
- DPM++ 2M
- DPM++ 2M Karras
- DPM++ 2M SDE
- DPM++ 2M SDE Karras
- DPM 3M
- DPM 3M Karras
- DPM 3M SDE
- DPM 3M Karras
- Euler
- Euler Karras
- Eular Ancestral
- Heun
- Heun Karras
- KDPM 2
- KDPM 2 Karras
- KDPM 2 Ancestral
- KDPM 2 Ancestral Karras
- LCM
- LMS
- LMS Karras
- PNDM
- TCD
- UniPC
- UniPC Karras

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/YourFeature`)  
3. Commit your changes (`git commit -m "Add ..."` )  
4. Push to your fork (`git push origin feature/YourFeature`)  
5. Open a Pull Request

## Contact

**Author:** Charles T Montgomery  
**Email:** charles.montgomery@hotmail.com  

---

*Happy prompting!*
