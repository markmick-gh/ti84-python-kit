# t84unit.py
# Simple unit conversions for TI-84 Python

IN_TO_CM = 2.54
FT_TO_M = 0.3048
MI_TO_KM = 1.60934
LB_TO_KG = 0.453592
OZ_TO_G = 28.3495
GAL_TO_L = 3.78541


def c_to_f(c):
    return (c * 9.0 / 5.0) + 32.0


def f_to_c(f):
    return (f - 32.0) * 5.0 / 9.0


def c_to_k(c):
    return c + 273.15


def k_to_c(k):
    return k - 273.15


def in_to_cm(inches):
    return inches * IN_TO_CM


def cm_to_in(cm):
    return cm / IN_TO_CM


def ft_to_m(ft):
    return ft * FT_TO_M


def m_to_ft(m):
    return m / FT_TO_M


def mi_to_km(mi):
    return mi * MI_TO_KM


def km_to_mi(km):
    return km / MI_TO_KM


def lb_to_kg(lb):
    return lb * LB_TO_KG


def kg_to_lb(kg):
    return kg / LB_TO_KG


def oz_to_g(oz):
    return oz * OZ_TO_G


def g_to_oz(g):
    return g / OZ_TO_G


def gal_to_l(gal):
    return gal * GAL_TO_L


def l_to_gal(liters):
    return liters / GAL_TO_L
