# Project Context – Detailed

This document contains the complete source code, documentation, and environment setup instructions for the **better_stable_diffusion_prompts** project. It is intended to be a single source of truth that can be used to reconstruct the entire repository from scratch, set up a Python virtual environment, and run the utility exactly as originally designed.

---

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Environment Setup](#environment-setup)  
3. [File Index](#file-index)  
   - [Root Files](#root-files)  
   - [Package Files](#package-files)  
4. [File Contents](#file-contents)  
   - [Root Files](#root-files-1)  
   - [Package Files](#package-files-1)  
5. [License](#license)  
6. [TODO](#todo)  

---

## Project Overview
`better_stable_diffusion_prompts` is a Python utility that builds Stable Diffusion prompts using Ollama. It supports both interactive and file‑based modes and can be executed either via the legacy `main.py` script or as a module (`python -m better_stable_diffusion_prompts`). The project is installable from source with `pip install .` and provides a console script entry point `better-stable-diffusion`.

---

## Environment Setup
The project relies **only on the Python standard library**; no third‑party packages are required.

### 1. Create a Python virtual environment
```bash
python3 -m venv .venv
```

### 2. Activate the virtual environment
```bash
source .venv/bin/activate
```
*All subsequent commands should be run while the virtual environment is active.*

### 3. Install requirements (if any)
```bash
pip install -r requirements.txt
```
> **Note:** `requirements.txt` currently contains only comments because the project has no external dependencies.

### 4. Verify the environment
```bash
python -m better_stable_diffusion_prompts --help
```
or run the legacy entry point:
```bash
./main.py --help
```

---

## File Index

### Root Files
| Path | Description |
|------|-------------|
| `cline.md` | This comprehensive context file (you are reading it). |
| `design.txt` | Design specification, scheduler list, and high‑level description of functionality. |
| `example1.txt` | Sample description used for prompt generation. |
| `LICENSE` | MIT license with explicit attribution and patent exclusion. |
| `README.md` | User‑facing documentation, installation, and usage guide. |
| `TODO` | Placeholder for future tasks (currently empty). |
| `setup.py` | setuptools configuration for packaging and installation. |
| `main.py` | Legacy entry point that forwards to the package’s `__main__`. |
| `requirements.txt` | Lists required Python packages (none for this project). |
| `better_stable_diffusion_prompts/` | Python package directory. |
| `.venv/` | Python virtual environment (created during setup). |

### Package Files (`better_stable_diffusion_prompts/`)
| Path | Description |
|------|-------------|
| `__init__.py` | Marks the directory as a Python package. |
| `__main__.py` | Implements the full CLI logic (interactive & file modes). |

---

## File Contents

### Root Files

#### `design.txt`
```text
Create a Python project that uses Ollama to progressively build a Stable Diffusion prompt.

The program accepts input in two ways:

1. **Interactive mode** – Input is received line by line until a line containing exactly **THE END** is encountered, then the program ends.
2. **File mode** – Command‑line arguments are treated as filenames. The files are read in the order provided, their contents are concatenated (newline‑separated), and the combined text is sent to Ollama in a single prompt (no **THE END** required).

For each input (whether interactive or from files), Ollama is given a prompt that builds a mental image and returns the following items:

* Positive Stable Diffusion prompt  
* Negative Stable Diffusion prompt  
* CFG Scale  
* Optimum Image Resolution  
* Steps (up to 500)  
* Scheduler (one of the listed options)

**Additional instruction** – The prompt now includes the phrase **“Use proper weights for drawn elements.”** to guide Ollama’s weighting of visual components.

**Model & CLI details**

* The prompt presented to Ollama references **model Juggernaut XL v9, no LoRA**.  
* The actual CLI call uses the `gemma3:27b` model (`ollama run gemma3:27b …`). This mismatch is intentional: the script keeps the placeholder CLI call while the prompt tells Ollama to assume the desired model.

**Output handling**

* An optional `-o <filename>` flag can be supplied; if present, the generated Stable Diffusion parameters are appended to the specified file in addition to being printed to stdout.

**Scheduler list (as per design)**

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

**Project state (as of 2025‑08‑24)**

* `main.py` implements both interactive and file modes, includes the `-o` output flag, and uses the placeholder CLI call described above.  
* The script falls back to deterministic placeholder output if the Ollama CLI invocation fails.  
* No code writes back to `cline.md`; all documentation is now stored explicitly in `design.txt` and `cline.md`.  
* The repository contains an example prompt description (`example1.txt`) and a comprehensive context file (`cline.md`) that aggregates all project artifacts.
```

#### `example1.txt`
```text
I am standing on a lush grassy field.
The are seven kilometer high mountains in the far distance.
The those mountains extend in both direction for a very great distance.
Between me an those mountains is a great circular lake.
Within that lake is elaborately geoenginered city.
The city is made of seven concentric circles of land each separated by elaborate canals.
In the center of the concentrics circles is an greater island.
There Are six lesser islands encircling the seventh  greater central island.
The six lesser islands each have a tall dark obsidian tower on top of them.
The seventh central and greater island has a great tall dark obsidian tower that reaches two kilometers high.
At the top of the great dark spire is bright iridescent light casting upwards a ray of great white light.
```

#### `LICENSE`
```text
MIT License

Copyright (c) 2025 Charles T Montgomery
All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

**DISCLAIMER OF WARRANTY**
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON‑INFRINGEMENT. THE ENTIRE RISK
TO THE QUALITY AND PERFORMANCE OF THE SOFTWARE IS WITH YOU. SHOULD THE
SOFTWARE PROVE DEFECTIVE, YOU ASSUME THE ENTIRE COST OF REPAIR OR
CORRECTION.

**LIMITATION OF LIABILITY**
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR ANY CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.

**EXPLICIT EXCLUSION (CRITICAL ADDITION)**
THIS LICENSE DOES NOT GRANT ANY RIGHTS TO USE, REPRODUCE, OR DISTRIBUTE ANY
PATENTED MATERIAL THAT MAY BE EMBEDDED OR REFERENCED BY THE SOFTWARE. THE
AUTHOR EXPLICITLY EXCLUDES ANY PATENT CLAIMS OR INTELLECTUAL PROPERTY RIGHTS
THAT ARE NOT COVERED BY THE MIT LICENSE TERMS.

**ATTRIBUTION**
Author: Charles T Montgomery  
Email: charles.montgomery@hotmail.com  
Year: 2025

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON‑INFRINGEMENT. THE ENTIRE RISK
TO THE QUALITY AND PERFORMANCE OF THE SOFTWARE IS WITH YOU. SHOULD THE
SOFTWARE PROVE DEFECTIVE, YOU ASSUME THE ENTIRE COST OF REPAIR OR
CORRECTION.
```

#### `README.md`
```markdown
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
--- End -------------------------------
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
```

#### `TODO`
*(currently empty)*

#### `setup.py`
```python
from setuptools import setup, find_packages

setup(
    name="better_stable_diffusion_prompts",
    version="0.1.0",
    description="Utility to build Stable Diffusion prompts using Ollama",
    author="Charles T Montgomery",
    author_email="charles.montgomery@hotmail.com",
    packages=find_packages(),
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "better-stable-diffusion=better_stable_diffusion_prompts.__main__:main",
        ],
    },
)
```

#### `main.py`
```python
#!/usr/bin/env python3
"""
Legacy entry point for Stable Diffusion Prompt Builder.

This wrapper forwards execution to the package entry point so that the
project can be run either as:
    python -m better_stable_diffusion_prompts [options] [filenames...]
or via the historic script:
    ./main.py [options] [filenames...]

All functionality is provided by the package's __main__.py.
"""

import sys
from better_stable_diffusion_prompts.__main__ import main as _main

if __name__ == "__main__":
    sys.exit(_main())
```

#### `requirements.txt`
```text
# No external Python dependencies required for this project.
# The project relies only on the Python standard library.
```

#### `better_stable_diffusion_prompts/__init__.py`
```python
# Package initialization for better_stable_diffusion_prompts
```

#### `better_stable_diffusion_prompts/__main__.py`
```python
#!/usr/bin/env python3
"""
Stable Diffusion Prompt Builder using Ollama.

This module can be executed as a script via:
    python -m better_stable_diffusion_prompts [options] [filenames...]

It supports two modes:
1. Interactive mode – reads lines from stdin until a line containing exactly "THE END".
2. File mode – accepts one or more filenames as command‑line arguments,
   concatenates their contents (newline‑separated), and sends the combined text
   to Ollama in a single prompt.
"""

import sys
import json
import subprocess
from typing import Dict, Any

# List of allowed schedulers (as per design.txt)
SCHEDULERS = [
    "DDIM", "DDPM", "DEIS", "DEIS Karras", "DPM++ 2S", "DPM++ 2S Karras",
    "DPM++ 2M", "DPM++ 2M Karras", "DPM++ 2M SDE", "DPM++ 2M SDE Karras",
    "DPM 3M", "DPM 3M Karras", "DPM 3M SDE", "DPM 3M Karras",
    "Euler", "Euler Karras", "Eular Ancestral", "Heun", "Heun Karras",
    "KDPM 2", "KDPM 2 Karras", "KDPM 2 Ancestral", "KDPM 2 Ancestral Karras",
    "LCM", "LMS", "LMS Karras", "PNDM", "TCD", "UniPC", "UniPC Karras"
]

def call_ollama(prompt: str) -> str:
    """
    Calls the Ollama CLI with the specified model and prompt.
    Returns the raw text output from Ollama.
    If the call fails, returns a deterministic placeholder string.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", "gemma3:27b", prompt],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception:
        # Placeholder output matching expected human‑readable format
        return (
            "Positive Prompt: placeholder positive prompt\\n"
            "Negative Prompt: placeholder negative prompt\\n"
            "CFG Scale: 7\\n"
            "Resolution: 512px\\n"
            "Steps: 50\\n"
            "Scheduler: DDIM"
        )

def main() -> None:
    # Optional output file handling (-o <filename>)
    output_file = None
    args = sys.argv[1:]

    # Detect and extract -o flag
    if "-o" in args:
        o_index = args.index("-o")
        if o_index + 1 < len(args):
            output_file = args[o_index + 1]
            # Remove flag and filename from args
            args = args[:o_index] + args[o_index + 2:]

    # If remaining args are filenames, process them
    if args:
        filenames = args
        try:
            contents = []
            for fname in filenames:
                with open(fname, "r", encoding="utf-8") as f:
                    contents.append(f.read())
            context = "\n".join(contents)
        except Exception as e:
            print(f"Error reading input files: {e}")
            sys.exit(1)

        ollama_prompt = (
            f"Based on the accumulated description:{context}\\n"
            "Use proper weights for drawn elements.\\n"
            "Provide the following items:\\n"
            "- Positive Stable Diffusion prompt\\n"
            "- Negative Stable Diffusion prompt\\n"
            "- CFG Scale\\n"
            "- Optimum Image Resolution\\n"
            "- Steps (up to 500)\\n"
            f"- Scheduler (choose from the allowed list): {', '.join(SCHEDULERS)}\\n"
            "Assume model Juggernaut XL v9, no LoRA."
        )
        output = call_ollama(ollama_prompt)

        print("\\n--- Generated Stable Diffusion Parameters ---")
        print(output)
        print("--- End --------------------------------------\\n")

        if output_file:
            try:
                with open(output_file, "a", encoding="utf-8") as out_f:
                    out_f.write(output + "\\n")
            except Exception as e:
                print(f"Failed to write output to {output_file}: {e}")

        sys.exit(0)

    # Interactive mode
    print("Enter lines of description (type 'THE END' on a line by itself to finish):")
    context = ""
    for line in sys.stdin:
        line = line.strip()
        if line == "THE END":
            break
        context += f"\\n{line}"
        ollama_prompt = (
            f"Based on the accumulated description:{context}\\n"
            "Use proper weights for drawn elements.\\n"
            "Provide the following items:\\n"
            "- Positive Stable Diffusion prompt\\n"
            "- Negative Stable Diffusion prompt\\n"
            "- CFG Scale\\n"
            "- Optimum Image Resolution\\n"
            "- Steps (up to 500)\\n"
            f"- Scheduler (choose from the allowed list): {', '.join(SCHEDULERS)}\\n"
            "Assume model Juggernaut XL v9, no LoRA."
        )
        output = call_ollama(ollama_prompt)

        print("\\n--- Generated Stable Diffusion Parameters ---")
        print(output)
        print("--- End --------------------------------------\\n")

        if output_file:
            try:
                with open(output_file, "a", encoding="utf-8") as out_f:
                    out_f.write(output + "\\n")
            except Exception as e:
                print(f"Failed to write output to {output_file}: {e}")

    print("Program terminated. No further input will be processed.")

if __name__ == "__main__":
    main()
```

### License
See `LICENSE` file above.

### TODO
*(currently empty)*
