# good_output_example.py
# Demonstrates improved TI-84 formatting and pagination

import t84disp

mass = 12.5
volume = 5.2
density = mass / volume

lines = []

# Title
lines.append("--------------------------------")
lines.append("        Lab Results")
lines.append("--------------------------------")
lines.append("")

# Intro text
wrapped = t84disp.wrap_text(
    "This version uses structured display "
    "functions to improve readability "
    "on the TI-84 screen."
)

lines.extend(wrapped)
lines.append("")

# Key values
lines.append("Sample Data")
lines.append(
    "Mass: " +
    t84disp.fmt_num(mass, 6, 2) +
    " g"
)

lines.append(
    "Volume: " +
    t84disp.fmt_num(volume, 6, 2) +
    " mL"
)

lines.append(
    "Density: " +
    t84disp.fmt_num(density, 6, 2) +
    " g/mL"
)

lines.append("")

# Table
lines.append("Trial Time Dist Vel")
lines.append("-------------------")
lines.append("1     1    5    5")
lines.append("2    10  125  12.5")
lines.append("3     2   17   8.5")

lines.append("")

# Conclusion
wrapped = t84disp.wrap_text(
    "Conclusion: structured output "
    "makes scientific results easier "
    "to read."
)

lines.extend(wrapped)

# Display with automatic pagination
t84disp.page_lines(lines)