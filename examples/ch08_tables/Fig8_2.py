# FIG8_2.py
# Structured scientific table
# Intended for Figure 8.2 screen capture

from t84disp import *

headers = ["t(s)", "h(m)", "v(m/s)"]

rows = [
    ["1", "4.9", "9.8"],
    ["2", "19.6", "19.6"],
    ["3", "44.1", "29.4"],
    ["10", "490.0", "98.0"]
]

show_table(headers, rows)

pause()