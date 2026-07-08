# FIG7_3.py
# Unit conversion workflow example
# Intended for Figure 7.3 screen capture

from t84disp import *
from t84unit import *

temp_c = 25.0

temp_f = c_to_f(temp_c)
temp_k = c_to_k(temp_c)

show_title("TEMP CONVERT")

show_kv("Celsius", fmt_num(temp_c, 6, 1) + " C")
show_kv("Fahrenheit", fmt_num(temp_f, 6, 1) + " F")
show_kv("Kelvin", fmt_num(temp_k, 6, 2) + " K")

pause()