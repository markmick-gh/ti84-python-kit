# FIG10_1.py
# Modular scientific workflow diagram
# Intended for Figure 10.1 screen capture

from ti_draw import *

def box(x, y, w, h, label):
    draw_line(x, y, x + w, y)
    draw_line(x + w, y, x + w, y + h)
    draw_line(x + w, y + h, x, y + h)
    draw_line(x, y + h, x, y)
    draw_text(x + 12, y + 6, label)

def arrow(x, y1, y2):
    draw_line(x, y1, x, y2)
    draw_line(x, y2, x - 5, y2 - 5)
    draw_line(x, y2, x + 5, y2 - 5)

clear()

set_color(0, 0, 0)
set_pen("thin", "solid")

# Title placed low enough to avoid the shell/status bar
draw_text(92, 28, "Modular Workflow")

# Boxes
box(85, 55, 150, 22, "INPUT")
box(85, 90, 150, 22, "CALC MODULE")
box(85, 125, 150, 22, "DISPLAY MODULE")
box(85, 160, 150, 22, "OUTPUT")

# Arrows
arrow(160, 77, 90)
arrow(160, 112, 125)
arrow(160, 147, 160)

show_draw()