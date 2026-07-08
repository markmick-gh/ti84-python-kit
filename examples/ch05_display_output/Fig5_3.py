# FIG5_3.py
# Compact scientific report example
# Intended for Figure 5.3 screen capture

from t84disp import *

mass = 12.5
volume = 5.2
density = mass / volume

pairs = [
    ["Mass", "12.5 g"],
    ["Volume", "5.2 mL"],
    ["Density", fmt_num(density, 6, 2) + " g/mL"]
]

show_record("DENSITY REPORT", pairs)

pause()