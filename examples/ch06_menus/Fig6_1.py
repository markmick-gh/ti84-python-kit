# FIG6_1.py
# Simple menu-driven scientific interface
# Intended for Figure 6.1 screen capture

from t84disp import *

show_title("SCI MENU")

options = [
    "Motion",
    "Density",
    "Gas Laws"
]

choice = menu_choice(options)

hr()
print("Choice: " + str(choice))

pause()