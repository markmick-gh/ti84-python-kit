# BBPRESS2.py
# Big Bear pressure plot with regression line

from ti_system import *
import ti_plotlib as plt


def main():
    elev_m = recall_list("1")
    press_hpa = recall_list("2")

    plt.cls()
    plt.auto_window(elev_m, press_hpa)
    plt.axes("on")
    plt.grid(500, 50, "dot")
    plt.title("P vs Elev")
    plt.labels("m", "hPa", 11, 2)
    plt.scatter(elev_m, press_hpa, "x")
    plt.lin_reg(elev_m, press_hpa, "right", 2)
#    plt.lin_reg(elev_m, press_hpa, "center", 2)
    plt.show_plot()
    plt.cls()

    print("slope =", round(plt.a, 3))
    print("int =", round(plt.b, 1))


main()