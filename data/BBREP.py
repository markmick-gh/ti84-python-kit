# BBREP.py
# Compact Big Bear field-data report
# Uses L1 = elevation_m, L2 = pressure_hPa

from ti_system import recall_list
import gc


def main():
    gc.collect()
    z = recall_list("1")
    gc.collect()
    p = recall_list("2")
    gc.collect()

    nz = len(z)
    np = len(p)

    print("BIG BEAR DATA")
    print("L1=", nz, " L2=", np)

    if nz != np:
        print("ERROR: unequal lists")
        print("Clear and reimport CSV")
        return

    if nz == 0:
        print("ERROR: empty lists")
        return

    zmin = z[0]
    zmax = z[0]
    pmin = p[0]
    pmax = p[0]

    sx = 0
    sy = 0
    sxx = 0
    sxy = 0

    i = 0
    while i < nz:
        x = z[i]
        y = p[i]

        if x < zmin:
            zmin = x
        if x > zmax:
            zmax = x
        if y < pmin:
            pmin = y
        if y > pmax:
            pmax = y

        sx = sx + x
        sy = sy + y
        sxx = sxx + x * x
        sxy = sxy + x * y

        i = i + 1

    den = nz * sxx - sx * sx

    if den == 0:
        print("ERROR: bad x data")
        return

    m = (nz * sxy - sx * sy) / den
    b = (sy - m * sx) / nz

    print("N=", nz)
    print("Elev min", round(zmin, 1))
    print("Elev max", round(zmax, 1))
    print("Press min", round(pmin, 1))
    print("Press max", round(pmax, 1))
    input("ENTER...")

    print("LINEAR MODEL")
    print("Slope", round(m, 4))
    print("hPa per km", round(m * 1000, 1))
    print("Intercept", round(b, 1))

    del z
    del p
    gc.collect()


main()
