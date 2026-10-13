# Super30 Euron Tasks

Setup and first Python program for the Super30 course.

## Environment setup

| Item | Details |
|---|---|
| Operating system | macOS (Apple Silicon) |
| Python version | 3.12.13 (output of `python --version`) |
| Environment manager | `uv`, with a virtual environment in `.venv` |
| Editor | Visual Studio Code 1.141.0 |
| VS Code extensions | Python (ms-python.python), Pylance (ms-python.vscode-pylance), Python Debugger (ms-python.debugpy), Jupyter (ms-toolsai.jupyter) |
| Terminal | VS Code integrated terminal, zsh |

## Setup steps

1. Install Python 3.12 with uv: `uv python install 3.12`
2. Create the virtual environment: `uv venv`
3. Activate it: `source .venv/bin/activate`
4. Check the interpreter: `python --version`, which prints `Python 3.12.13`
5. In VS Code, select the interpreter with `Cmd+Shift+P`, then "Python: Select Interpreter", then `.venv`.

## Project structure

```
.
├── README.md
├── pyproject.toml      # project metadata, requires Python >= 3.12
├── .python-version     # pins Python 3.12
├── requirements.txt
└── super30-python/
    └── hello.py        # first program
```

## Running the program

```bash
source .venv/bin/activate
python super30-python/hello.py
```

Expected output:

```
Hello Super30
My Python environment is ready
Python version: 3.12.13 (main, May 10 2026, 19:20:41) [Clang 22.1.3 ]
System: Darwin 27.0.0 (arm64)
```
