# FIG4_3.py
# Key-value display example

from t84disp import *

mass = 12.5
volume = 5.2
density = mass / volume

show_title("SAMPLE DATA")

show_kv("Mass (g)", fmt_num(mass, 6, 1))
show_kv("Volume (mL)", fmt_num(volume, 6, 1))
show_kv("Density", fmt_num(density, 6, 2))

pause()