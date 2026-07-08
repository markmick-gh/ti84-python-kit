# BBPRESS.py
# Big Bear elevation-pressure analysis
# Import BB_6-27_ti84_alt_pressure.csv to L1/L2 first.

from ti_system import *
from math import *
import ti_plotlib as plt


def linreg(x, y):
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sxx = 0
    sxy = 0
    i = 0
    while i < n:
        sxx = sxx + x[i] * x[i]
        sxy = sxy + x[i] * y[i]
        i = i + 1
    den = n * sxx - sx * sx
    b = (n * sxy - sx * sy) / den
    a = (sy - b * sx) / n
    ybar = sy / n
    ssr = 0
    sst = 0
    i = 0
    while i < n:
        yp = a + b * x[i]
        ssr = ssr + (y[i] - yp) ** 2
        sst = sst + (y[i] - ybar) ** 2
        i = i + 1
    r2 = 1 - ssr / sst
    return a, b, r2


def main():
    z = recall_list("1")
    p = recall_list("2")
    n = len(z)

    lp = []
    i = 0
    while i < n:
        lp.append(log(p[i]))
        i = i + 1

    a, b, r2 = linreg(z, lp)
    p0 = exp(a)
    H = -1 / b

    print("BIG BEAR DATA")
    print("N=", n)
    print("P0=", round(p0, 1), "hPa")
    print("H=", round(H, 0), "m")
    print("R2=", round(r2, 4))
    input("ENTER...")

    plt.cls()
    plt.window(0, 2700, 740, 1020)
    plt.axes("on")
    plt.labels("m", "hPa", 12, 2)
    plt.title("P vs ELEV")
    plt.scatter(z, p, "o")
    plt.show_plot()


main()
