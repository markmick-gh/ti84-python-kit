# FIG8_3.py
# Experimental data table
# Intended for Figure 8.3 screen capture

from t84disp import *

headers = ["Trial", "Temp", "pH"]

rows = [
    ["1", "22.1", "6.85"],
    ["2", "22.4", "6.88"],
    ["3", "22.0", "6.84"],
    ["4", "22.3", "6.87"]
]

show_table(headers, rows)

pause()