# FIG9_1.py
# Interactive system control example
# Intended for Figure 9.1 screen capture

from t84disp import *
from ti_system import *

show_title("KEY CONTROL")

print("Press any key")
print("to continue...")
hr()
print("Waiting...")

key = wait_key()

hr()
print("Key code:")
print(str(key))

pause()