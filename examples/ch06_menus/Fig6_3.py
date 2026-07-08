# FIG6_3.py
# Input validation example
# Intended for Figure 6.3 screen capture

from t84disp import *

show_title("MASS CHECK")

mass = float(input("Mass (g): "))

if mass <= 0:
    hr()
    show_text("Invalid input. Mass must be greater than zero.")
else:
    hr()
    show_kv("Mass", fmt_num(mass, 6, 2) + " g")

pause()