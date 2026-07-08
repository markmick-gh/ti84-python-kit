# FIG8_5.py
# Left versus right numerical alignment
# Intended for Figure 8.5 screen capture

from t84disp import *

print("NUMBER ALIGNMENT")
hr()

print(pad_right("Left", 10) + pad_left("Right", 10))
print(pad_right("1.2", 10) + pad_left("1.2", 10))
print(pad_right("12.5", 10) + pad_left("12.5", 10))
print(pad_right("125.0", 10) + pad_left("125.0", 10))

pause()