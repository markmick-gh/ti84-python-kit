# FIG10_2.py
# Temporary debugging output example
# Intended for Figure 10.2 screen capture

from t84disp import *

distance = 100.0
time_s = 9.58

# Calculation being checked
speed = distance / time_s

show_title("DEBUG VALUES")

show_kv("DEBUG d", fmt_num(distance, 7, 2) + " m")
show_kv("DEBUG t", fmt_num(time_s, 7, 2) + " s")
show_kv("DEBUG v", fmt_num(speed, 7, 3) + " m/s")

pause()