# ex01_test.py
#
# Basic test/demo program for the TI-84 display library.
#
# This file demonstrates:
#   - Titles
#   - Horizontal rules
#   - Key/value formatting
#   - Wrapped text
#   - Tables
#   - Menu input
#   - Pagination
#
# Intended for use with:
#   display/display.py
#

from display import *


def test_title():
    show_title("DISPLAY LIB TEST")


def test_wrapped_text():
    text = (
        "This is a long paragraph intended to test the "
        "text wrapping functionality of the display "
        "library on the TI-84 Python environment."
    )

    show_text(text)


def test_key_value():
    show_title("KEY/VALUE TEST")

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
        ["Temp", "22 C"],
    ]

    show_table(headers, rows)

    pause()


def test_paging():
    show_title("PAGING TEST")

    lines = []

    for i in range(1, 21):
        lines.append("Line {}".format(i))

    show_lines(lines)


def test_menu():
    show_title("MENU TEST")

    options = [
        "Run Example A",
        "Run Example B",
        "Exit",
    ]

    choice = menu_choice("Select Option", options)

    hr()
    print("Choice:", choice)

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
