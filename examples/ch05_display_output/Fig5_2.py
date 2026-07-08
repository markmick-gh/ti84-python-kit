# FIG5_2.py
# Structured paged output example
# Intended for Figure 5.2 screen capture

from t84disp import *

lines = [
    "TEMP DATA PAGE 1",
    "--------------------------",
    "1  Temp 21.4 C",
    "2  Temp 21.8 C",
    "3  Temp 22.1 C",
    "TEMP DATA PAGE 2",
    "--------------------------",
    "4  Temp 22.5 C",
    "5  Temp 22.9 C",
    "6  Temp 23.2 C"
]

page_lines(lines, 5)