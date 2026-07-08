# FIG9_2.py
# Basic graphics display using ti_draw
# Intended for Figure 9.2 screen capture

from ti_draw import *

clear()

# Title moved lower to avoid shell/status bar
set_color(0, 0, 0)
draw_text(95, 28, "Cooling Data")

# Axes shifted down slightly
set_pen("thin", "solid")
draw_line(40, 190, 280, 190)   # x-axis
draw_line(40, 60, 40, 190)     # y-axis

draw_text(285, 184, "t")
draw_text(22, 55, "T")

# Trend line
set_pen("medium", "solid")
draw_line(60, 85, 100, 105)
draw_line(100, 105, 140, 125)
draw_line(140, 125, 180, 140)
draw_line(180, 140, 220, 152)
draw_line(220, 152, 260, 160)

# Data points
fill_circle(60, 85, 4)
fill_circle(100, 105, 4)
fill_circle(140, 125, 4)
fill_circle(180, 140, 4)
fill_circle(220, 152, 4)
fill_circle(260, 160, 4)

show_draw()