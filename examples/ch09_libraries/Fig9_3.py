# FIG9_3.py
# Scientific plotting using ti_plotlib
# Intended for Figure 9.3 screen capture

import ti_plotlib as plt

# Cooling data
time = [0, 1, 2, 3, 4, 5]
temp = [24.0, 22.8, 21.9, 21.1, 20.6, 20.2]

plt.cls()

# xmin, xmax, ymin, ymax
plt.window(0, 5, 19, 25)

plt.axes("on")
plt.grid(1, 1, "dot")
plt.title("Cooling")

# Draw connecting line segments first
plt.pen("medium", "solid")
plt.line(0, 24.0, 1, 22.8, "")
plt.line(1, 22.8, 2, 21.9, "")
plt.line(2, 21.9, 3, 21.1, "")
plt.line(3, 21.1, 4, 20.6, "")
plt.line(4, 20.6, 5, 20.2, "")

# Plot points second so they remain visible
plt.scatter(time, temp, "o")

plt.show_plot()