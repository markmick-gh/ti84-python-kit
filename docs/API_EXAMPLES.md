# Physics Examples

```python
import ti_phys
import ti_display

v = ti_phys.speed(100, 9.58)

ti_display.show_kv("Speed", v)
```

Output:

```text
Speed: 10.44
```

---

# ti_phys Examples

## speed()

```python
import ti_phys
import ti_display

v = ti_phys.speed(100, 9.58)

ti_display.show_kv("Speed", v)
```

---

## acceleration()

```python
import ti_phys

a = ti_phys.acceleration(20, 4)

print(a)
```

---

## force()

```python
import ti_phys

f = ti_phys.force(10, 9.8)

print(f)
```

---

## weight()

```python
import ti_phys

w = ti_phys.weight(70)

print(w)
```

---

## work()

```python
import ti_phys

w = ti_phys.work(50, 10)

print(w)
```

---

## power()

```python
import ti_phys

p = ti_phys.power(500, 20)

print(p)
```

---

## kinetic_energy()

```python
import ti_phys

ke = ti_phys.kinetic_energy(2, 5)

print(ke)
```

---

## potential_energy()

```python
import ti_phys

pe = ti_phys.potential_energy(3, 10)

print(pe)
```

---

## density()

```python
import ti_phys

d = ti_phys.density(25, 5)

print(d)
```

---

## pressure()

```python
import ti_phys

p = ti_phys.pressure(100, 2)

print(p)
```

---

## wave_speed()

```python
import ti_phys

v = ti_phys.wave_speed(440, 0.78)

print(v)
```


# Chemistry Examples

---

# ti_chem Examples

## moles_from_mass()

```python
import ti_chem

moles = ti_chem.moles_from_mass(18, 18.015)

print(moles)
```

---

## mass_from_moles()

```python
import ti_chem

mass = ti_chem.mass_from_moles(2, 58.44)

print(mass)
```

---

## molarity()

```python
import ti_chem

m = ti_chem.molarity(0.5, 1.0)

print(m)
```

---

## moles_from_molarity()

```python
import ti_chem

moles = ti_chem.moles_from_molarity(2.0, 0.25)

print(moles)
```

---

## dilution_m1v1()

```python
import ti_chem

m2 = ti_chem.dilution_m1v1(
    6.0,
    25.0,
    100.0
)

print(m2)
```

---

## percent_mass()

```python
import ti_chem

pct = ti_chem.percent_mass(5, 100)

print(pct)
```

---

## ph_from_h3o()

```python
import ti_chem

ph = ti_chem.ph_from_h3o(1e-3)

print(ph)
```

---

## h3o_from_ph()

```python
import ti_chem

h3o = ti_chem.h3o_from_ph(3)

print(h3o)
```

---

## ideal_gas_pressure()

```python
import ti_chem

p = ti_chem.ideal_gas_pressure(
    1.0,
    22.4,
    273
)

print(p)
```

---

## ideal_gas_volume()

```python
import ti_chem

v = ti_chem.ideal_gas_volume(
    1.0,
    1.0,
    273
)

print(v)
```


# Units Examples

# ti_units Examples

## c_to_f()

```python
import ti_units

f = ti_units.c_to_f(25)

print(f)
```

---

## f_to_c()

```python
import ti_units

c = ti_units.f_to_c(98.6)

print(c)
```

---

## c_to_k()

```python
import ti_units

k = ti_units.c_to_k(25)

print(k)
```

---

## k_to_c()

```python
import ti_units

c = ti_units.k_to_c(300)

print(c)
```

---

## in_to_cm()

```python
import ti_units

cm = ti_units.in_to_cm(10)

print(cm)
```

---

## cm_to_in()

```python
import ti_units

inch = ti_units.cm_to_in(25.4)

print(inch)
```

---

## ft_to_m()

```python
import ti_units

m = ti_units.ft_to_m(6)

print(m)
```

---

## m_to_ft()

```python
import ti_units

ft = ti_units.m_to_ft(3)

print(ft)
```

---

## mi_to_km()

```python
import ti_units

km = ti_units.mi_to_km(10)

print(km)
```

---

## km_to_mi()

```python
import ti_units

mi = ti_units.km_to_mi(16)

print(mi)
```

---

## lb_to_kg()

```python
import ti_units

kg = ti_units.lb_to_kg(150)

print(kg)
```

---

## kg_to_lb()

```python
import ti_units

lb = ti_units.kg_to_lb(68)

print(lb)
```

---

## oz_to_g()

```python
import ti_units

g = ti_units.oz_to_g(12)

print(g)
```

---

## g_to_oz()

```python
import ti_units

oz = ti_units.g_to_oz(100)

print(oz)
```

---

## gal_to_l()

```python
import ti_units

liters = ti_units.gal_to_l(2)

print(liters)
```

---

## l_to_gal()

```python
import ti_units

gal = ti_units.l_to_gal(5)

print(gal)
```


# Display Examples

---

# ti_display Examples

## pause()

```python
import ti_display

print("Program complete.")
ti_display.pause()
```

---

## hr()

```python
import ti_display

ti_display.hr()
print("Section 1")
ti_display.hr("=")
```

---

## clear_lines()

```python
import ti_display

print("Before clear")
ti_display.clear_lines()
print("After clear")
```

---

## fit_line()

```python
import ti_display

s = ti_display.fit_line(
    "This line is too long for the TI-84 screen."
)

print(s)
```

---

## wrap_text()

```python
import ti_display

lines = ti_display.wrap_text(
    "The TI-84 screen has limited width."
)

print(lines)
```

---

## page_lines()

```python
import ti_display

lines = [
    "Line 1",
    "Line 2",
    "Line 3",
    "Line 4",
    "Line 5",
    "Line 6",
    "Line 7",
    "Line 8"
]

ti_display.page_lines(lines)
```

---

## show_lines()

```python
import ti_display

lines = [
    "Hydrogen",
    "Helium",
    "Lithium"
]

ti_display.show_lines(lines)
```

---

## show_text()

```python
import ti_display

ti_display.show_text(
    "Physics and chemistry calculations can "
    "be displayed cleanly on the TI-84."
)
```

---

## show_title()

```python
import ti_display

ti_display.show_title("Gas Law Results")
```

---

## fmt_num()

```python
import ti_display

s = ti_display.fmt_num(3.14159265)

print(s)
```

---

## show_kv()

```python
import ti_display

ti_display.show_kv("Speed", 10.44)
```

---

## show_record()

```python
import ti_display

pairs = [
    ("Mass", "12.5 g"),
    ("Volume", "5.2 mL"),
    ("Density", "2.40 g/mL")
]

ti_display.show_record("Sample Data", pairs)
```

---

## menu_choice()

```python
import ti_display

options = [
    "Physics",
    "Chemistry",
    "Quit"
]

choice = ti_display.menu_choice(options)

print(choice)
```

---

## show_table()

```python
import ti_display

headers = ["Time", "Dist"]

rows = [
    ["1", "5"],
    ["2", "10"],
    ["3", "15"]
]

ti_display.show_table(headers, rows)
```

