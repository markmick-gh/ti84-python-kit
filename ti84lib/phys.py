# phys.py
# Basic physics helpers for TI-84 Python

G = 9.8                 # m/s^2
C = 3.00e8              # m/s


def speed(distance_m, time_s):
    return distance_m / time_s


def acceleration(delta_v_m_s, time_s):
    return delta_v_m_s / time_s


def force(mass_kg, acceleration_m_s2):
    return mass_kg * acceleration_m_s2


def weight(mass_kg):
    return mass_kg * G


def work(force_n, distance_m):
    return force_n * distance_m


def power(work_j, time_s):
    return work_j / time_s


def kinetic_energy(mass_kg, speed_m_s):
    return 0.5 * mass_kg * speed_m_s * speed_m_s


def potential_energy(mass_kg, height_m):
    return mass_kg * G * height_m


def density(mass, volume):
    return mass / volume


def pressure(force_n, area_m2):
    return force_n / area_m2


def wave_speed(frequency_hz, wavelength_m):
    return frequency_hz * wavelength_m
