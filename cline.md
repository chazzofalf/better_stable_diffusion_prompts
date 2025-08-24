# Project Context – Detailed

## Overview
`better_stable_diffusion_prompts` is a Python utility that builds Stable Diffusion prompts using Ollama.  
It can be executed in two ways:

1. **Legacy script** – `./main.py` (or `python main.py`) – preserved for backward compatibility.  
2. **Module execution** – `python -m better_stable_diffusion_prompts` – the preferred modern entry point.

Both entry points provide identical functionality:
* **Interactive mode** – reads description lines from STDIN until a line containing exactly `THE END`.  
* **File mode** – accepts one or more filenames, concatenates their contents (newline‑separated), and sends the combined text to Ollama in a single request.  

An optional `-o <filename>` flag appends the generated parameters to the specified file in addition to printing them.

## Package Layout
```
better_stable_diffusion_prompts/
│   __init__.py          # Marks the directory as a package
│   __main__.py          # Implements the full CLI logic
main.py                    # Thin wrapper that forwards to the package entry point
README.md                  # User‑facing documentation
design.txt                 # Design specification (scheduler list, prompt format, etc.)
example1.txt               # Sample description file
LICENSE
cline.md                   # This detailed context file
```

### `better_stable_diffusion_prompts/__main__.py`
* Contains the full implementation previously in `main.py`.  
* Exposes a `main()` function that is called when the module is executed via `python -m better_stable_diffusion_prompts`.  
* Handles argument parsing, `-o` flag detection, file reading, interactive loop, prompt construction, Ollama CLI invocation, and result output.

### `main.py`
* Legacy entry point that simply imports and calls `better_stable_diffusion_prompts.__main__.main`.  
* Ensures existing scripts or tutorials that invoke `./main.py` continue to work unchanged.

## Scheduler List
The allowed schedulers (as defined in `design.txt`) are:

- DDIM, DDPM, DEIS, DEIS Karras, DPM++ 2S, DPM++ 2S Karras, DPM++ 2M, DPM++ 2M Karras, DPM++ 2M SDE, DPM++ 2M SDE Karras, DPM 3M, DPM 3M Karras, DPM 3M SDE, DPM 3M Karras, Euler, Euler Karras, Eular Ancestral, Heun, Heun Karras, KDPM 2, KDPM 2 Karras, KDPM 2 Ancestral, KDPM 2 Ancestral Karras, LCM, LMS, LMS Karras, PNDM, TCD, UniPC, UniPC Karras

## Prompt Construction (sent to Ollama)
For every request the tool builds a prompt of the form:

```
Based on the accumulated description:<context>
Use proper weights for drawn elements.
Provide the following items:
- Positive Stable Diffusion prompt
- Negative Stable Diffusion prompt
- CFG Scale
- Optimum Image Resolution
- Steps (up to 500)
- Scheduler (choose from the allowed list): <comma‑separated list>
Assume model Juggernaut XL v9, no LoRA.
```

If the Ollama CLI is unavailable or fails, a deterministic placeholder output is returned:

```
Positive Prompt: placeholder positive prompt
Negative Prompt: placeholder negative prompt
CFG Scale: 7
Resolution: 512px
Steps: 50
Scheduler: DDIM
```

## Installation & Usage

1. **Clone the repository** (already done in the current workspace).  
2. **Ensure Python 3.9+** is installed – the project uses only the standard library.  
3. **(Optional) Install Ollama** for real model calls.  

### Run as a module (recommended)

```bash
python -m better_stable_diffusion_prompts [options] [filenames...]
```

### Run via legacy script

```bash
./main.py [options] [filenames...]
```

### Example (file mode)

```bash
python -m better_stable_diffusion_prompts example1.txt -o output.txt
```

### Example (interactive mode)

```bash
python -m better_stable_diffusion_prompts
Enter lines of description (type 'THE END' on a line by itself to finish):
...
THE END
```

## License
MIT – see the `LICENSE` file.

## Contributing
Standard GitHub workflow: fork, branch, commit, push, pull request.

## Contact
**Author:** Charles T Montgomery  
**Email:** charles.montgomery@hotmail.com  

---  

*This `cline.md` file now contains the complete, up‑to‑date context for the project, including package structure, entry points, scheduler list, prompt format, usage instructions, and contribution guidelines.*
