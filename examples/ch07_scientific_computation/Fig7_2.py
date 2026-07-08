# FIG7_2.py
# Excessive numerical precision example
# Intended for Figure 7.2 screen capture

from t84disp import *

mass = 12.5
volume = 5.2
density = mass / volume

print("PRECISION")
hr()

print("RAW:")
print(str(density) + " g/mL")

print("FORMATTED:")
print(fmt_num(density, 6, 2) + " g/mL")

pause()