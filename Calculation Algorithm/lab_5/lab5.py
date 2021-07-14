from numpy.polynomial.legendre import leggauss
import numpy as np
from math import pi, exp, sin, cos
import matplotlib.pyplot as plt

LIMITS = [[0, pi / 2], [0, pi / 2]]

def converts(func2, value):
    return lambda y: func2(value, y)

def variable_conversion(a, b, t):
    return (b + a) / 2 + (b - a) * t / 2

def function(parameter):
    return lambda x, y: (4 / pi) * (1 - exp(-parameter * 2 * cos(x) / (1 - (sin(x) ** 2) * (cos(y) ** 2)))) * cos(x) * sin(x)

def gauss(func, a, b, amounts):
    args, coeffs = leggauss(amounts)
    res = 0

    for i in range(amounts):
        res += (b - a) / 2 * coeffs[i] * func(variable_conversion(a, b, args[i]))

    return res

def simpson(func, a, b, amounts):
    if (amounts < 3 or amounts & 1 == 0):
        raise ValueError
    h = (b - a) / (amounts - 1)
    x = a
    res = 0

    for i in range((amounts - 1) // 2):
        res += func(x) + 4 * func(x + h) + func(x + 2 * h)
        x += 2 * h

    return res * (h / 3)

def result(func, n, m, tao):
    return simpson(lambda x: gauss(converts(func, x), LIMITS[1][0], LIMITS[1][1], m), LIMITS[0][0], LIMITS[0][1], n)

def main():
    N = int(input("Input N: "))
    M = int(input("Input M: "))
    tao = float(input("Input t: "))

    print("result: ", result(function(tao), N, M, tao))

def graph():
    plt.grid(True)
    plt.xlabel("t")
    plt.ylabel("e")
    N = 5
    M = 5
    T = np.arange(0.05, 10, 0.05)
    E = [result(function(tao), N, M, tao) for tao in T]
    plt.plot(T, E, "k")
    plt.show()

main()
graph()
