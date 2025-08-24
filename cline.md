# Project Context

## Overview
This repository implements a **Stable Diffusion Prompt Builder** using Ollama.  
The core script (`main.py`) can operate in two modes:

1. **Interactive mode** – reads lines from stdin until a line containing exactly `THE END` is entered.  
2. **File mode** – accepts one or more filenames as command‑line arguments, concatenates their contents (newline‑separated), and sends the combined text to Ollama in a single prompt.

For each input (interactive line or concatenated file text) Ollama is prompted to generate:

* Positive Stable Diffusion prompt  
* Negative Stable Diffusion prompt  
* CFG Scale  
* Optimum Image Resolution  
* Steps (up to 500)  
* Scheduler (chosen from a predefined list)

The prompt always includes the instruction **“Use proper weights for drawn elements.”** and references **model Juggernaut XL v9, no LoRA**.  
The actual CLI call uses the placeholder model `gemma3:27b` (`ollama run gemma3:27b …`). If the Ollama CLI fails, a deterministic placeholder output is returned.

An optional `-o <filename>` flag allows the generated parameters to be appended to a file in addition to stdout.

---

## Design Specification (design.txt)

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

---

## Example Prompt (example1.txt)

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

---

## Source Code (main.py)

#!/usr/bin/env python3
\"\"\"
Stable Diffusion Prompt Builder using Ollama.

This script reads lines from standard input until a line containing exactly "THE END" is encountered.
For each input line, it sends a prompt to an Ollama model (Juggernaut XL v9) to progressively build a
mental image and then outputs a set of parameters suitable for a Stable Diffusion generation.
\"\"\"

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
    \"\"\"
    Calls the Ollama CLI with the specified model and prompt.
    Returns the raw text output from Ollama.
    If the call fails, returns a deterministic placeholder string.
    \"\"\"
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

def main():
    # Optional output file handling (-o <filename>)
    output_file = None
    # Determine if an output file flag is present
    args = sys.argv[1:]
    if "-o" in args:
        o_index = args.index("-o")
        if o_index + 1 < len(args):
            output_file = args[o_index + 1]
            # Remove the flag and filename from args
            args = args[:o_index] + args[o_index + 2:]
    # Remaining args are treated as input filenames (if any)
    if len(args) > 0:
        filenames = args
        # Read and concatenate file contents with newline separation
        try:
            contents = []
            for fname in filenames:
                with open(fname, "r", encoding="utf-8") as f:
                    contents.append(f.read())
            context = "\\n".join(contents)
        except Exception as e:
            print(f"Error reading input files: {e}")
            sys.exit(1)

        # Build prompt for Ollama using the full concatenated context
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

        # Output the generated parameters
        print("\\n--- Generated Stable Diffusion Parameters ---")
        print(output)
        print("--- End --------------------------------------\\n")

        # If an output file was specified, write the output there as well
        if output_file:
            try:
                with open(output_file, "a", encoding="utf-8") as out_f:
                    out_f.write(output + "\\n")
            except Exception as e:
                print(f"Failed to write output to {output_file}: {e}")

        # Exit after processing file inputs
        sys.exit(0)

    # No command‑line arguments: fall back to interactive line‑by‑line mode
    print("Enter lines of description (type 'THE END' on a line by itself to finish):")
    context = ""
    for line in sys.stdin:
        line = line.strip()
        if line == "THE END":
            break
        # Append to mental context
        context += f"\\n{line}"
        # Build prompt for Ollama
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

        # Output the generated parameters
        print("\\n--- Generated Stable Diffusion Parameters ---")
        print(output)
        print("--- End --------------------------------------\\n")

        # If an output file was specified, write the output there as well
        if output_file:
            try:
                with open(output_file, "a", encoding="utf-8") as out_f:
                    out_f.write(output + "\\n")
            except Exception as e:
                print(f"Failed to write output to {output_file}: {e}")

        # Context saving removed (interactive mode)

    print("Program terminated. No further input will be processed.")
    print("Enter lines of description (type 'THE END' on a line by itself to finish):")
    context = ""
    for line in sys.stdin:
        line = line.strip()
        if line == "THE END":
            break
        # Append to mental context
        context += f"\\n{line}"
        # Build prompt for Ollama
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
        # Build prompt for Ollama
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

        # Output the generated parameters
        print("\\n--- Generated Stable Diffusion Parameters ---")
        print(output)
        print("--- End --------------------------------------\\n")

        # Context saving removed (interactive mode)

    print("Program terminated. No further input will be processed.")

if __name__ == "__main__":
    main()
