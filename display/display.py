# display.py

MAX_COLS = 26
MAX_ROWS = 7

def pause():
    input("ENTER...")

def show_lines(lines):
    count = 0
    for line in lines:
        print(line)
        count += 1
        if count >= MAX_ROWS:
            pause()
            count = 0
