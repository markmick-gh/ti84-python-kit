# FIG4_2.py
# Improved output example

from t84disp import *
from t84chem import *

mass = 1.2534
mm = 58.44
vol = 0.0357
temp_c = 22.6
temp_k = temp_c + 273.15

mol = moles_from_mass(mass, mm)
M = molarity(mol, vol)
P = ideal_gas_pressure(mol, 1.25, temp_k)

show_title("NaCl DATA")

print("mass g " + fmt_num(mass, 8, 4))
print("mol    " + fmt_num(mol, 8, 4))
print("vol L  " + fmt_num(vol, 8, 4))
print("M      " + fmt_num(M, 8, 3))
print("P atm  " + fmt_num(P, 8, 3))

pause()