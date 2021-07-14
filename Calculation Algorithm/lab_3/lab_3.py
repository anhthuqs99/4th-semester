from math import cos

def f(x):
    return x**3 - 2 * x**2 - 4

def get_table(x_beg, step, amount):
    x_tbl = [x_beg + step * i for i in range(amount)]
    y_tbl = [f(x) for x in  x_tbl]

    return x_tbl, y_tbl

def print_table(x, y):
    for i in range(len(x)):
        print("%.4f %.4f" % (x[i], y[i]))
    print()

def interpolate(x, y, x_value):
    n = len(x)
    i_near = min(range(n), key = lambda i: abs(x[i] - x_value)) #index of nearest x value

    h = [0 if not i else x[i] - x[i - 1] for i in range(n)] #step value

    A = [0 if i < 2 else h[i - 1] for i in range(n)]
    B = [0 if i < 2 else -2 * (h[i - 1] + h[i]) for i in range(n)]
    D = [0 if i < 2 else h[i] for i in range(n)]
    F = [0 if i < 2 else -3 * ((y[i] - y[i - 1]) / h[i] - (y[i - 1] - y[i - 2]) / h[i - 1]) for i in range(n)]

    ksi = [0 for i in range(n + 1)]
    eta = [0 for i in range(n + 1)]

    #forward
    for i in range(2, n):
        ksi[i + 1] = D[i] / (B[i] - A[i] * ksi[i])
        eta[i + 1] = (A[i] * eta[i] + F[i]) / (B[i] - A[i] * ksi[i])
    
    #backward
    c = [0 for i in range(n + 1)]
    for i in range(n - 2, -1, -1):
        c[i] = ksi[i + 1] * c[i + 1] + eta[i + 1]

    a = [0 if i < 1 else y[i - 1] for i in range(n)]
    b = [0 if i < 1 else ((y[i] - y[i - 1]) / h[i]) - (h[i] / 3) * (c[i + 1] + 2 * c[i]) for i in range(n)]
    d = [0 if i < 1 else (c[i + 1] - c[i]) / (3 * h[i]) for i in range(n)]

    # print(h,"\n", A, "\n", B, "\n", D, "\n", F,"\n")
    # print(ksi, "\n", eta, "\n")
    # print(a, "\n", b, "\n", c, "\n", d, "\n")

    ai = a[i_near]
    bi = b[i_near]
    ci = c[i_near]
    di = d[i_near]
    hi = x_value - x[i_near - 1]
    return ai + bi * hi + ci * hi**2 + di * hi**3

x_beg = float(input("Вводить начальное значение x: "))
x_step = float(input("Вводить шаг: "))
x_amount = int(input("Вводить количество точки:"))

x_tbl, y_tbl = get_table(x_beg, x_step, x_amount)
print("Таблица значения:")
print_table(x_tbl, y_tbl)

x = float(input("Вводить значение x: "))

result = interpolate(x_tbl, y_tbl, x)
print("Интерполяция: ", result)
print("F(x)        : ", f(x))
print("Error       : ", abs(f(x) - result))
