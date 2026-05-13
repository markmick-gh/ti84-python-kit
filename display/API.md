## Screen Limits

The library assumes:

* 26 columns
* 7 visible rows

Constants:

```python
MAX_COLS
MAX_ROWS
```

---

## Functions

### pause()

Wait for ENTER key.

```python
pause()
```

---

### hr()

Display a horizontal rule.

```python
hr()
```

Optional character:

```python
hr("=")
```

---

### clear_lines()

Print blank lines.

```python
clear_lines()
```

---

### fit_line()

Trim text to screen width.

```python
s = fit_line(text)
```

---

### wrap_text()

Wrap text into a list of lines.

```python
lines = wrap_text(text)
```

---

### page_lines()

Display lines with automatic paging.

```python
page_lines(lines)
```

---

### show_lines()

Shortcut for page_lines().

```python
show_lines(lines)
```

---

### show_text()

Wrap and display a paragraph.

```python
show_text(text)
```

---

### show_title()

Centered title with horizontal rules.

```python
show_title("MY TITLE")
```

---

### fmt_num()

Simple numeric formatting.

```python
s = fmt_num(3.14159)
```

---

### show_kv()

Display a key/value pair.

```python
show_kv("Voltage", "5.0 V")
```

---

### show_record()

Display a record of label/value pairs.

```python
pairs = [
    ["Mass", "12.5 g"],
    ["Volume", "8.0 mL"]
]

show_record("DATA", pairs)
```

---

### menu_choice()

Display a numbered menu and return selection.

```python
options = [
    "Option A",
    "Option B",
    "Exit"
]

choice = menu_choice(options)
```

---

### show_table()

Display a simple fixed-width table.

```python
headers = ["Item", "Value"]

rows = [
    ["Mass", "12.5 g"],
    ["Temp", "22 C"]
]

show_table(headers, rows)
```

---

## Notes

* Designed specifically for TI-84 Plus CE Python calculators
* Avoids unsupported desktop Python features
* Compatible with TI MicroPython environment

````
