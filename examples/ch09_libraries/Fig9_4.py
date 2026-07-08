# FIG9_4.py
# Processing experimental data in calculator list L1
# Intended for Figure 9.4 screen capture

from ti_system import *
from t84disp import *

# Demo data stored into calculator list L1
# L1 contains repeated temperature measurements.
data = [22.1, 22.4, 22.0, 22.3]
store_list("1", data)

# Recall calculator list L1 into Python
temps = recall_list("1")

n = len(temps)
total = 0
min_t = temps[0]
max_t = temps[0]

i = 0
while i < n:
    value = temps[i]
    total = total + value

    if value < min_t:
        min_t = value

    if value > max_t:
        max_t = value

    i = i + 1

avg = total / n
range_t = max_t - min_t

# Build compact list display
line = "L1:"
i = 0
while i < n:
    line = line + " " + fmt_num(temps[i], 4, 1)
    i = i + 1

print("TEMP LIST L1")
hr()
print(fit_line(line))
print("N=" + str(n) + " Avg=" + fmt_num(avg, 5, 2) + " C")
print("Min=" + fmt_num(min_t, 5, 2) + " Max=" + fmt_num(max_t, 5, 2))
print("Range=" + fmt_num(range_t, 4, 2) + " C")

pause()