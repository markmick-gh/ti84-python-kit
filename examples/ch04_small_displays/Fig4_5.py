# FIG4_5.py
# Compact scientific table example

from t84disp import *

headers = ["t(s)", "d(m)", "v(m/s)"]

rows = [
    ["1", "4.9", "9.8"],
    ["2", "19.6", "19.6"],
    ["3", "44.1", "29.4"],
    ["4", "78.4", "39.2"]
]

show_table(headers, rows)

pause()