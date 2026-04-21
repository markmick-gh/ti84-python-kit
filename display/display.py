# display.py
# TI-84 Python Display Utilities (v1.0)
#
# Provides simple formatting and paging utilities for the TI-84 screen.
# All output should use these functions instead of raw print().

MAX_COLS = 26
MAX_ROWS = 7


# ---------------------------
# Core control
# ---------------------------

def pause():
    input("ENTER...")


def hr(char="-"):
    print(char * MAX_COLS)


def clear_lines(n=MAX_ROWS):
    for _ in range(n):
        print("")


# ---------------------------
# Text formatting
# ---------------------------

def fit_line(text, width=MAX_COLS):
    s = str(text)
    if len(s) <= width:
        return s
    return s[:width]


def wrap_text(text, width=MAX_COLS):
    words = str(text).split()
    lines = []
    line = ""

    for word in words:
        if len(line) == 0:
            trial = word
        else:
            trial = line + " " + word

        if len(trial) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            # hard split long word
            while len(word) > width:
                lines.append(word[:width])
                word = word[width:]
            line = word

    if line:
        lines.append(line)

    return lines


# ---------------------------
# Paging
# ---------------------------

def page_lines(lines, rows=MAX_ROWS):
    count = 0
    for line in lines:
        print(line)
        count += 1
        if count >= rows:
            pause()
            count = 0


def show_lines(lines):
    page_lines(lines)


def show_text(text):
    lines = wrap_text(text)
    page_lines(lines)


# ---------------------------
# Display helpers
# ---------------------------

def show_title(title):
    hr()
    print(fit_line(title.center(MAX_COLS)))
    hr()


def fmt_num(x, width=6, precision=2):
    try:
        s = str(round(float(x), precision))
    except:
        s = str(x)

    if len(s) > width:
        s = s[:width]

    return s.rjust(width)


def show_kv(label, value):
    text = str(label) + ": " + str(value)
    show_text(text)


def show_record(title, pairs):
    show_title(title)
    lines = []
    for label, value in pairs:
        line = str(label) + ": " + str(value)
        lines.extend(wrap_text(line))
    page_lines(lines)


def menu_choice(options):
    # options = ["Option 1", "Option 2", ...]
    lines = []
    for i, opt in enumerate(options, start=1):
        line = str(i) + ": " + str(opt)
        lines.append(fit_line(line))

    page_lines(lines)

    try:
        choice = int(input("Choice: "))
        if 1 <= choice <= len(options):
            return choice
    except:
        pass

    return None


def show_table(headers, rows):
    # Simple narrow table
    col_width = int(MAX_COLS / len(headers)) - 1

    def fmt_cell(x):
        s = str(x)
        if len(s) > col_width:
            s = s[:col_width]
        return s.ljust(col_width)

    # header
    header_line = " ".join([fmt_cell(h) for h in headers])
    lines = [header_line]
    lines.append("-" * len(header_line))

    # rows
    for row in rows:
        line = " ".join([fmt_cell(x) for x in row])
        lines.append(line)

    page_lines(lines)
