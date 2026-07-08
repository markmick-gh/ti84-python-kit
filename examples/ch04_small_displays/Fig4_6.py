# FIG4_6.py
# Paged output example

from t84disp import *

lines = [
    "FIELD DATA",
    "--------------------------",
    "1  Temp 21.4 C",
    "2  Temp 21.8 C",
    "3  Temp 22.1 C",
    "4  Temp 22.5 C",
    "5  Temp 22.9 C",
    "6  Temp 23.2 C",
    "7  Temp 23.6 C",
    "8  Temp 24.0 C",
    "9  Temp 24.3 C",
    "10 Temp 24.7 C"
]

show_lines(lines)

pause()