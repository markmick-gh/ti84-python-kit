# FIG6_2.py
# Scientific input prompt example
# Intended for Figure 6.2 screen capture

from t84disp import *

show_title("DENSITY INPUT")

mass = float(input("Mass (g): "))
volume = float(input("Vol (mL): "))

density = mass / volume

hr()
show_kv("Density", fmt_num(density, 6, 2) + " g/mL")

pause()