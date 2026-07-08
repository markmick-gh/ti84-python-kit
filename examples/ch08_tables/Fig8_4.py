# FIG8_4.py
# Structured scientific summary
# Intended for Figure 8.4 screen capture

from t84disp import *

t1 = 22.1
t2 = 22.4
t3 = 22.0
t4 = 22.3

avg = (t1 + t2 + t3 + t4) / 4.0
min_t = 22.0
max_t = 22.4

pairs = [
    ["Avg Temp", fmt_num(avg, 6, 2) + " C"],
    ["Min Temp", fmt_num(min_t, 6, 2) + " C"],
    ["Max Temp", fmt_num(max_t, 6, 2) + " C"]
]

show_record("TEMP SUMMARY", pairs)

pause()