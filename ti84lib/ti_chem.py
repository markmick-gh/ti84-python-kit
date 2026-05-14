# ti_chem.py
# Basic chemistry helpers for TI-84 Python

AVOGADRO = 6.022e23
R_GAS = 0.0821       # L atm / mol K
R_J = 8.314          # J / mol K


def moles_from_mass(mass_g, molar_mass_g_mol):
    return mass_g / molar_mass_g_mol


def mass_from_moles(moles, molar_mass_g_mol):
    return moles * molar_mass_g_mol


def molarity(moles, volume_l):
    return moles / volume_l


def moles_from_molarity(molarity_m, volume_l):
    return molarity_m * volume_l


def dilution_m1v1(m1, v1, v2):
    return (m1 * v1) / v2


def percent_mass(solute_g, solution_g):
    return (solute_g / solution_g) * 100.0


def ph_from_h3o(h3o_m):
    import math
    return -math.log10(h3o_m)


def h3o_from_ph(ph):
    return 10 ** (-ph)


def ideal_gas_pressure(n, volume_l, temp_k):
    return (n * R_GAS * temp_k) / volume_l


def ideal_gas_volume(n, pressure_atm, temp_k):
    return (n * R_GAS * temp_k) / pressure_atm
