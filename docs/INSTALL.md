# Installation Guide

This guide explains how to install the TI-84 Python Kit
onto a TI-84 Plus CE Python calculator.

---

# Requirements

Hardware:

- TI-84 Plus CE Python calculator
- USB cable

Software:

- TI Connect CE
- Python App installed on calculator

---

# Download the Project

Option 1:

Clone with Git:

```bash
git clone https://github.com/markmick-gh/ti84-python-kit.git
```

Option 2:

Download ZIP from GitHub:

1. Open the project page
2. Click "Code"
3. Click "Download ZIP"
4. Extract the ZIP file

---

# Files Needed

Minimum required files:

```text
display/display.py
examples/ex01_test.py
```

---

# Connect the Calculator

1. Launch TI Connect CE
2. Connect the calculator using USB
3. Wait for the calculator to appear

---

# Send Files to Calculator

In TI Connect CE:

1. Open "Calculator Explorer"
2. Drag these files into the calculator:

```text
display.py
ex01_test.py
```

Important:

- Send the actual `.py` files
- Do NOT send folders
- Do NOT preserve folder structure

TI-84 Python imports operate as flat files.

---

# Run the Example

On the calculator:

1. Open the Python App
2. Select:

```text
ex01_test.py
```

3. Press Run

---

# Expected Output

The test program demonstrates:

- Titles
- Wrapped text
- Key/value display
- Tables
- Menus
- Paging

---

# Troubleshooting

## Import Errors

If you see:

```text
ImportError
```

confirm that:

- `display.py` exists on the calculator
- import statement is:

```python
from display import *
```

---

## Unsupported Method Errors

The TI-84 uses a limited MicroPython implementation.

Some desktop Python features are unsupported.

See:

```text
docs/LIMITATIONS.md
```

---

# Updating Files

If a file changes:

1. Delete old version from calculator
2. Re-send updated `.py` file

This avoids stale file issues.

---

# Recommended Workflow

Recommended local workflow:

```text
Desktop Python Editor
        ↓
TI Connect CE
        ↓
TI-84 Calculator
```

Recommended editors:

- VS Code
- Spyder
- Thonny
- Notepad++
