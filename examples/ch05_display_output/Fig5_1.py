# FIG5_1.py
# Continuous output without pagination
# Intended for Figure 5.1 screen capture

print("TEMP LOGGER RAW OUTPUT")
print("No pauses or pages")
print("")

i = 1
temp = 21.4

while i <= 16:
    print("sample " + str(i) + " temp_C=" + str(temp))
    temp = temp + 0.37
    i = i + 1

input("ENTER...")