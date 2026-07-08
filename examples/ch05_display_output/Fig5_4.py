# FIG5_4.py
# Multi-page scientific table
# Intended for Figure 5.4 screen capture

from t84disp import *

headers = ["t(s)", "h(m)", "v(m/s)"]

rows = [
    ["0", "0.0", "0.0"],
    ["1", "4.9", "9.8"],
    ["2", "19.6", "19.6"],
    ["3", "44.1", "29.4"],
    ["4", "78.4", "39.2"],
    ["5", "122.5", "49.0"],
    ["6", "176.4", "58.8"],
    ["7", "240.1", "68.6"],
    ["8", "313.6", "78.4"],
    ["9", "396.9", "88.2"],
    ["10", "490.0", "98.0"]
]

show_table(headers, rows)

pause()