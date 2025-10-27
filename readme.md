# Advanced Calculator Application
---


## Installation Instructions

### 1. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate

```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Configuration Setup

Create a `.env` file in the project root with the following variables:

```bash
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=2
CALCULATOR_MAX_INPUT_VALUE=1e6
CALCULATOR_DEFAULT_ENCODING=utf-8
```

---

## Features

### Arithmetic Operations
- Addition, Subtraction, Multiplication, Division
- Power
- Root
- Modulus
- Integer Division
- Percentage
- Absolute Difference

### Design Patterns Used
- Factory Pattern — for creating operation instances.
- Memento Pattern — for managing undo/redo in history.
- Observer Pattern — for logging and auto-saving history.

### Additional Features
- Undo/Redo functionality
- Logging and auto-save via observers
- Input validation and error handling
- Configurable settings via `.env` file

---

## Usage Guide

Run the calculator REPL interface:
```bash
python -m app
```

### Available Commands
| Command | Description |
|----------|-------------|
| add, subtract, multiply, divide | Basic arithmetic |
| power | Exponentiation |
| root | Nth root of a number |
| modulus | Remainder of division |
| int_divide | Integer division |
| percent | Percentage calculation |
| abs_diff | Absolute difference |
| history | Show calculation history |
| clear | Clear calculation history |
| undo / redo | Undo or redo last operation |
| save / load | Save or load history to/from CSV |
| help | Show available commands |
| exit | Quit the program |



---

## CI/CD with GitHub Actions

The project includes a GitHub Actions workflow file located at:
```
.github/workflows/python-app.yml
```


---

## License
This project is for educational purposes only.
