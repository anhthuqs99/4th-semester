from algorithms_test import *


# Draws graphs of time efficiency of different algs
def time_test(n):
    circles = []

    time_canon = []
    time_param = []
    time_br = []
    time_mid = []
    time_std = []
    r_mas = []

    for r in range(1, n, 10000):
        circles.append([5000, 5000, r])
        r_mas.append(r)

    for c in circles:
        time_canon.append(test_circle_canon(c[0], c[1], c[2]))
        time_param.append(test_circle_param(c[0], c[1], c[2]))
        time_br.append(test_circle_br(c[0], c[1], c[2]))
        time_mid.append(test_circle_mid(c[0], c[1], c[2]))
        time_std.append(test_circle_std(c[0], c[1], c[2]))

    return time_canon, time_param, time_br, time_mid, time_std, r_mas