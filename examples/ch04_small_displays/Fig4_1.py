# FIG4_1.py
# Cluttered raw output example
# Intended for screen capture

from t84chem import *

mass = 1.2534
mm = 58.44
vol = 0.0357
temp_c = 22.6
temp_k = temp_c + 273.15

mol = moles_from_mass(mass, mm)
M = molarity(mol, vol)
P = ideal_gas_pressure(mol, 1.25, temp_k)

print("RAW CHEM OUTPUT")
print("mass="+str(mass)+"g mm="+str(mm)+"g/mol")
print("mol="+str(mol)+"vol="+str(vol)+"L")
print("M="+str(M)+" tempC="+str(temp_c))
print("tempK="+str(temp_k)+" P="+str(P))
print("atm n="+str(mol)+" V=1.25")
print("done")