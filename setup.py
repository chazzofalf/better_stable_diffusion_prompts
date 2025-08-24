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
