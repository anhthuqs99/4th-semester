import matplotlib.pyplot as plt
import numpy as np

def f(x_arr, coeff):
    res = np.zeros(len(x_arr))
    for i in range(len(coeff)):
        res += coeff[i] * (x_arr**i)
        
    return res

#read datas from file
def read_from_file(filename):
    f = open(filename, "r")
    N = list(map(int, f.readline().split()))
    x, y, ro = [], [], []
    for line in f:
        line = line.split(" ")
        x.append(float(line[0]))
        y.append(float(line[1]))
        ro.append(float(line[2]))
    return N, x, y, ro

def print_table(x, y, ro):
    print("%10s%10s%10s" % ("x", "y", "ro"))
    for i in range(len(x)):
        print("%10.2f%10.2f%10.2f" % (x[i], y[i], ro[i]))

    print()

def print_matr(matr):
    for line in matr:
        for value in line:
            print("%8.2f" % (value), end = '')
        print()

#Calculate
def root_mean_square(x, y, ro, n):
    length = len(x)
    sum_x_n = [sum([x[i]**j*ro[i] for i in range(length)]) for j in range(n * 2 - 1)]
    sum_y_x_n = [sum([x[i]**j*ro[i]*y[i] for i in range(length)]) for j in range(n)]
    matr = [sum_x_n[i:i+n] for i in range(n)]

    for i in range(n):
        matr[i].append(sum_y_x_n[i])

    return Gauss(matr)

def Gauss(matr):
    n = len(matr)

    for k in range(n):
        for i in range(k + 1, n):
            coeff = - (matr[i][k] / matr[k][k])
            for j in range(k, n + 1):
                matr[i][j] += coeff * matr[k][j]

    print("\nTriangled:")
    print_matr(matr)

    a = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            matr[i][n] -= a[j] * matr[i][j]
        a[i] = matr[i][n] / matr[i][i]

    return a

#Draw graphics
def show(a, x, y, ro, n):
    t = np.arange(-5, 5, 0.04)
    #plt.figure(1)
    plt.ylabel("y")
    plt.xlabel("x")
    plt.plot(t, f(t, a), label = LINENAME[n - 1], lw = 0.7)
    for i in range(len(x)):
        plt.plot(x[i], y[i], "ro", markersize = ro[i] + 2)

def process(filename): 
    N, x, y, ro = read_from_file(filename)
    print("Таблица функции с весами: ")
    print_table(x, y, ro)
    for n in N:
        a = root_mean_square(x, y, ro, n + 1)
        print("\na: ", end = '')
        for value in a:
            print("%8.2f" % (value), end = '')
        print()
        show(a, x, y , ro, n)
    plt.legend()
    plt.grid(True)
#Task 1:
LINENAME = ["p1", "p2","p3", "p4"]
process("data.txt")
plt.show()

#Task 2:
LINENAME = ["Веса всех точек одинаковы "]
process("data1.txt")
LINENAME = ["Веса точек разные"]
process("data2.txt")
plt.show()
