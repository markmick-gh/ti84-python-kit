# display.py
# TI-84 Python Display Utilities
# MicroPython-safe version

MAX_COLS = 26
MAX_ROWS = 7


def pause():
    input("ENTER...")


def hr(char="-"):
    print(char * MAX_COLS)


def clear_lines(n=MAX_ROWS):
    i = 0
    while i < n:
        print("")
        i = i + 1


def fit_line(text, width=MAX_COLS):
    s = str(text)
    if len(s) <= width:
        return s
    return s[:width]


def pad_right(text, width):
    s = str(text)
    if len(s) > width:
        return s[:width]

    while len(s) < width:
        s = s + " "

    return s


def pad_left(text, width):
    s = str(text)
    if len(s) > width:
        return s[:width]

    while len(s) < width:
        s = " " + s

    return s


def center_line(text, width=MAX_COLS):
    s = str(text)
    if len(s) > width:
        return s[:width]

    left = int((width - len(s)) / 2)
    line = ""

    i = 0
    while i < left:
        line = line + " "
        i = i + 1

    line = line + s
    return line


def wrap_text(text, width=MAX_COLS):
    words = str(text).split()
    lines = []
    line = ""

    i = 0
    while i < len(words):
        word = words[i]

        if len(line) == 0:
            trial = word
        else:
            trial = line + " " + word

        if len(trial) <= width:
            line = trial
        else:
            if len(line) > 0:
                lines.append(line)

            while len(word) > width:
                lines.append(word[:width])
                word = word[width:]

            line = word

        i = i + 1

    if len(line) > 0:
        lines.append(line)

    return lines


def page_lines(lines, rows=MAX_ROWS):
    count = 0
    i = 0

    while i < len(lines):
        print(lines[i])
        count = count + 1

        if count >= rows:
            pause()
            count = 0

        i = i + 1


def show_lines(lines):
    page_lines(lines)


def show_text(text):
    lines = wrap_text(text)
    page_lines(lines)


def show_title(title):
    hr()
    print(center_line(title))
    hr()


def fmt_num(x, width=6, precision=2):
    try:
        value = float(x)
        mult = 10 ** precision
        value = int(value * mult + 0.5) / mult
        s = str(value)
    except:
        s = str(x)

    if len(s) > width:
        s = s[:width]

    return pad_left(s, width)


def show_kv(label, value):
    text = str(label) + ": " + str(value)
    show_text(text)


def show_record(title, pairs):
    show_title(title)

    lines = []
    i = 0

    while i < len(pairs):
        pair = pairs[i]
        line = str(pair[0]) + ": " + str(pair[1])
        wrapped = wrap_text(line)

        j = 0
        while j < len(wrapped):
            lines.append(wrapped[j])
            j = j + 1

        i = i + 1

    page_lines(lines)


def menu_choice(options):
    lines = []
    i = 0

    while i < len(options):
        line = str(i + 1) + ": " + str(options[i])
        lines.append(fit_line(line))
        i = i + 1

    page_lines(lines)

    try:
        choice = int(input("Choice: "))
        if choice >= 1 and choice <= len(options):
            return choice
    except:
        pass

    return None


def make_table_line(items, col_width):
    line = ""
    i = 0

    while i < len(items):
        if i > 0:
            line = line + " "
        line = line + pad_right(items[i], col_width)
        i = i + 1

    return fit_line(line)


def show_table(headers, rows):
    if len(headers) <= 0:
        return

    col_width = int(MAX_COLS / len(headers)) - 1

    if col_width < 1:
        col_width = 1

    lines = []

    header_line = make_table_line(headers, col_width)
    lines.append(header_line)
    lines.append("-" * len(header_line))

    i = 0
    while i < len(rows):
        row_line = make_table_line(rows[i], col_width)
        lines.append(row_line)
        i = i + 1

    page_lines(lines)