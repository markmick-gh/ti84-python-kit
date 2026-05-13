# TI-84 MicroPython Limitations

The TI-84 Plus CE Python calculator uses a restricted
MicroPython environment.

This project intentionally avoids many standard desktop
Python features to maximize compatibility.

---

# Important Differences

The TI-84 Python environment is NOT full CPython.

Code that works on a desktop computer may fail on the calculator.

---

# Unsupported or Unreliable Features

The following features may not work correctly.

---

## Advanced String Methods

Some string methods are unsupported.

Examples:

```python
text.center(20)
text.ljust(20)
text.rjust(20)
```

This project uses manual padding instead.

---

## Package-Style Imports

Folder/package imports are unreliable.

Avoid:

```python
from display.display import *
```

Use:

```python
from display import *
```

All files should exist at the top calculator level.

---

## f-Strings

f-strings may not work reliably.

Avoid:

```python
f"Value = {x}"
```

Use:

```python
"Value = " + str(x)
```

---

## enumerate(start=...)

Advanced enumerate usage may fail.

Avoid:

```python
enumerate(items, start=1)
```

Use manual indexing instead.

---

## Complex List Comprehensions

Simple list comprehensions may work.

Complex nested versions may fail or consume excess memory.

---

## Nested Functions

Nested helper functions may behave inconsistently.

Prefer top-level functions.

---

## Memory Constraints

The calculator has limited RAM.

Avoid:

- large lists
- large strings
- recursion
- deep nesting

---

# Screen Constraints

The display library assumes:

```text
26 columns
7 rows
```

Programs should be designed around these limits.

---

# File System Constraints

Calculator Python files behave differently from desktop systems.

Important rules:

- flat file structure only
- avoid subpackages
- filenames should remain short
- avoid spaces in filenames

---

# Performance Constraints

The TI-84 CPU is slow compared to desktop systems.

Avoid:

- heavy floating-point math
- large loops
- large tables
- complex parsing

---

# Recommended Coding Style

For maximum compatibility:

- use simple loops
- avoid advanced syntax
- avoid decorators
- avoid generators
- avoid metaprogramming
- avoid large libraries

---

# Design Goal of This Project

The TI-84 Python Kit is intentionally conservative.

The library prioritizes:

1. reliability
2. readability
3. compatibility
4. educational simplicity

over advanced Python features.
