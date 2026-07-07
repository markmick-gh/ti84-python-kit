# ex01_test.py
# Basic test/demo program for TI-84 t84disp.py
# MicroPython-safe version

from t84disp import *


def test_title():
    show_title("DISPLAY LIB TEST")
    pause()


def test_wrapped_text():
    show_title("WRAP TEST")

    text = (
        "This is a long paragraph intended to test the "
        "text wrapping function on the TI-84 Python screen."
    )

    show_text(text)
    pause()


def test_key_value():
    show_title("KEY VALUE TEST")

    show_kv("Voltage", "5.0 V")
    show_kv("Current", "0.25 A")
    show_kv("Resistance", "20 ohm")

    pause()


def test_table():
    show_title("TABLE TEST")

    headers = ["Item", "Value"]

    rows = [
        ["Mass", "12.5 g"],
        ["Volume", "8.0 mL"],
        ["Density", "1.56"],
        ["Temp", "22 C"]
    ]

    show_table(headers, rows)
    pause()


def test_paging():
    show_title("PAGING TEST")

    lines = []
    i = 1

    while i <= 20:
        lines.append("Line " + str(i))
        i = i + 1

    show_lines(lines)
    pause()


def test_menu():
    show_title("MENU TEST")

    options = [
        "Run Example A",
        "Run Example B",
        "Exit"
    ]

    choice = menu_choice(options)

    hr()
    print("Choice: " + str(choice))

    pause()


def main():
    test_title()
    test_wrapped_text()
    test_key_value()
    test_table()
    test_paging()
    test_menu()

    show_title("TEST COMPLETE")


main()
