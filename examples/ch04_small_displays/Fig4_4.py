# FIG4_4.py
# Wrapped text display example

from t84disp import *

raw = "LongScientificMessagesCanRunPastTheScreenEdge"

msg = (
    "Long scientific messages should wrap "
    "at word boundaries for readability."
)

print("RAW OUTPUT")
print(raw)
hr()
print("WRAPPED")
show_text(msg)

pause()