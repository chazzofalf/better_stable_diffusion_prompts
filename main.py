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
