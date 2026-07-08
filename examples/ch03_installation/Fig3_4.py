# good_output_example.py
# Structured output using t84disp.py

import t84disp

mass = 12.34567
volume = 3.21
density = mass / volume
temp_c = 24.8
temp_k = temp_c + 273.15

t84disp.show_title("DENSITY LAB")

t84disp.show_kv("mass g", t84disp.fmt_num(mass))
t84disp.show_kv("volume mL", t84disp.fmt_num(volume))
t84disp.show_kv("density", t84disp.fmt_num(density))
t84disp.show_kv("temp C", t84disp.fmt_num(temp_c))
t84disp.show_kv("temp K", t84disp.fmt_num(temp_k))

t84disp.hr()
t84disp.show_text("Values are rounded for t84disp. Use full precision in calculations.")