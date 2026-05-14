# ti_phys Physics Examples

## acceleration()

```python
import ti_phys
import ti_display

a = ti_phys.acceleration(20, 4)

ti_display.show_kv(
    "Acceleration (m/s^2)",
    a
)
```

---

## force()

```python
import ti_phys
import ti_display

f = ti_phys.force(10, 9.8)

ti_display.show_kv(
    "Force (N)",
    f
)
```

---

## weight()

```python
import ti_phys
import ti_display

w = ti_phys.weight(70)

ti_display.show_kv(
    "Weight (N)",
    w
)
```

---

## work()

```python
import ti_phys
import ti_display

w = ti_phys.work(50, 10)

ti_display.show_kv(
    "Work (J)",
    w
)
```

---

## power()

```python
import ti_phys
import ti_display

p = ti_phys.power(500, 20)

ti_display.show_kv(
    "Power (W)",
    p
)
```

---

## kinetic_energy()

```python
import ti_phys
import ti_display

ke = ti_phys.kinetic_energy(2, 5)

ti_display.show_kv(
    "Kinetic Energy (J)",
    ke
)
```

---

## potential_energy()

```python
import ti_phys
import ti_display

pe = ti_phys.potential_energy(3, 10)

ti_display.show_kv(
    "Potential Energy (J)",
    pe
)
```

---

## density()

```python
import ti_phys
import ti_display

d = ti_phys.density(25, 5)

ti_display.show_kv(
    "Density",
    d
)
```

---

## pressure()

```python
import ti_phys
import ti_display

p = ti_phys.pressure(100, 2)

ti_display.show_kv(
    "Pressure (Pa)",
    p
)
```

---

## wave_speed()

```python
import ti_phys
import ti_display

v = ti_phys.wave_speed(440, 0.78)

ti_display.show_kv(
    "Wave Speed (m/s)",
    v
)
```

---

# ti_chem Chemistry Examples

## moles_from_mass()

```python
import ti_chem
import ti_display

moles = ti_chem.moles_from_mass(
    18,
    18.015
)

ti_display.show_kv(
    "Moles",
    moles
)
```

---

## mass_from_moles()

```python
import ti_chem
import ti_display

mass = ti_chem.mass_from_moles(
    2,
    58.44
)

ti_display.show_kv(
    "Mass (g)",
    mass
)
```

---

## molarity()

```python
import ti_chem
import ti_display

m = ti_chem.molarity(0.5, 1.0)

ti_display.show_kv(
    "Molarity (M)",
    m
)
```

---

## moles_from_molarity()

```python
import ti_chem
import ti_display

moles = ti_chem.moles_from_molarity(
    2.0,
    0.25
)

ti_display.show_kv(
    "Moles",
    moles
)
```

---

## dilution_m1v1()

```python
import ti_chem
import ti_display

m2 = ti_chem.dilution_m1v1(
    6.0,
    25.0,
    100.0
)

ti_display.show_kv(
    "Diluted Molarity",
    m2
)
```

---

## percent_mass()

```python
import ti_chem
import ti_display

pct = ti_chem.percent_mass(5, 100)

ti_display.show_kv(
    "Mass Percent (%)",
    pct
)
```

---

## ph_from_h3o()

```python
import ti_chem
import ti_display

ph = ti_chem.ph_from_h3o(1e-3)

ti_display.show_kv(
    "pH",
    ph
)
```

---

## h3o_from_ph()

```python
import ti_chem
import ti_display

h3o = ti_chem.h3o_from_ph(3)

ti_display.show_kv(
    "[H3O+]",
    h3o
)
```

---

## ideal_gas_pressure()

```python
import ti_chem
import ti_display

p = ti_chem.ideal_gas_pressure(
    1.0,
    22.4,
    273
)

ti_display.show_kv(
    "Pressure (atm)",
    p
)
```

---

## ideal_gas_volume()

```python
import ti_chem
import ti_display

v = ti_chem.ideal_gas_volume(
    1.0,
    1.0,
    273
)

ti_display.show_kv(
    "Volume (L)",
    v
)
```

---

# ti_units Units Examples

## c_to_f()

```python
import ti_units
import ti_display

f = ti_units.c_to_f(25)

ti_display.show_kv(
    "Temperature (F)",
    f
)
```

---

## f_to_c()

```python
import ti_units
import ti_display

c = ti_units.f_to_c(98.6)

ti_display.show_kv(
    "Temperature (C)",
    c
)
```

---

## c_to_k()

```python
import ti_units
import ti_display

k = ti_units.c_to_k(25)

ti_display.show_kv(
    "Temperature (K)",
    k
)
```

---

## k_to_c()

```python
import ti_units
import ti_display

c = ti_units.k_to_c(300)

ti_display.show_kv(
    "Temperature (C)",
    c
)
```

---

## in_to_cm()

```python
import ti_units
import ti_display

cm = ti_units.in_to_cm(10)

ti_display.show_kv(
    "Length (cm)",
    cm
)
```

---

## cm_to_in()

```python
import ti_units
import ti_display

inch = ti_units.cm_to_in(25.4)

ti_display.show_kv(
    "Length (in)",
    inch
)
```

---

## ft_to_m()

```python
import ti_units
import ti_display

m = ti_units.ft_to_m(6)

ti_display.show_kv(
    "Length (m)",
    m
)
```

---

## m_to_ft()

```python
import ti_units
import ti_display

ft = ti_units.m_to_ft(3)

ti_display.show_kv(
    "Length (ft)",
    ft
)
```

---

## mi_to_km()

```python
import ti_units
import ti_display

km = ti_units.mi_to_km(10)

ti_display.show_kv(
    "Distance (km)",
    km
)
```

---

## km_to_mi()

```python
import ti_units
import ti_display

mi = ti_units.km_to_mi(16)

ti_display.show_kv(
    "Distance (mi)",
    mi
)
```

---

## lb_to_kg()

```python
import ti_units
import ti_display

kg = ti_units.lb_to_kg(150)

ti_display.show_kv(
    "Mass (kg)",
    kg
)
```

---

## kg_to_lb()

```python
import ti_units
import ti_display

lb = ti_units.kg_to_lb(68)

ti_display.show_kv(
    "Mass (lb)",
    lb
)
```

---

## oz_to_g()

```python
import ti_units
import ti_display

g = ti_units.oz_to_g(12)

ti_display.show_kv(
    "Mass (g)",
    g
)
```

---

## g_to_oz()

```python
import ti_units
import ti_display

oz = ti_units.g_to_oz(100)

ti_display.show_kv(
    "Mass (oz)",
    oz
)
```

---

## gal_to_l()

```python
import ti_units
import ti_display

liters = ti_units.gal_to_l(2)

ti_display.show_kv(
    "Volume (L)",
    liters
)
```

---

## l_to_gal()

```python
import ti_units
import ti_display

gal = ti_units.l_to_gal(5)

ti_display.show_kv(
    "Volume (gal)",
    gal
)
```
