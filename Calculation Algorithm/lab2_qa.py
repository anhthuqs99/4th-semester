import sys
import numpy as np
from math import *

f = lambda x, y : x**2 + x*y - 3*y

def initMatrix():
    x_start = 0
    x_stop = 2.5
    x_num = 6
    y_start = 5
    y_stop = 7.5
    y_num = 6
    x = np.linspace(x_start, x_stop, x_num)
    y = np.linspace(y_start, y_stop, y_num)
    z = [[f(j, i) for i in y] for j in x]
    return x, y, z

def printMatrix(x, y, z):
    print("     x\\y", end=' ')
    for i in y:
        print('{:8g}'.format(i), end=' ')
    print()
    for i in range(x.size):
        print('{:8g}'.format(x[i]), end=' ')
        for j in range(y.size):
            print('{:8g}'.format(z[i][j]), end=' ')
        print()
    print()

def initDividedDifferenceTable(points, number_of_nodes, value):
    # greater than or equal to the value
    ge_index = next(a[0] for a in enumerate(points) if a[1][0] >= value)
    start_index = max(0, ge_index - number_of_nodes//2)
    end_index = min(len(points) - 1, ge_index + number_of_nodes//2)

    if end_index == len(points) - 1:
        start_index = len(points) - number_of_nodes

    table = points[start_index:start_index+number_of_nodes]
    table = [list(i) for i in table]
    return table

def completeDividedDifferenceTable(points, number_of_nodes, value):
    table = initDividedDifferenceTable(points, number_of_nodes, value)
    count = number_of_nodes - 1
    for j in range(2, number_of_nodes + 2):
        for i in range(0, count):
            table[i].append((table[i][j - 1] - table[i + 1][j - 1]) / (table[i][0] - table[i + j - 1][0]))
        count -= 1
    return table

def computeNewtonPolynomial(points, degree_of_polynomial, value):
    table = completeDividedDifferenceTable(points, degree_of_polynomial + 1, value)
    coefficient = 1
    result = 0
    for i in range(0, degree_of_polynomial + 1):
        result += coefficient * table[0][i + 1]
        coefficient *= (value - table[i][0])
    return result

def computeBilinearInterpolation(x, y, z, x_degree, y_degree, x_val, y_val):
    res = [computeNewtonPolynomial(list(zip(y, z[i])), y_degree, y_val) for i in range(x.size)]
    res = list(zip(x, res))
    return computeNewtonPolynomial(res, x_degree, x_val)



#Init the matrix
x, y, z = initMatrix()
printMatrix(x, y, z)
#Input the value x
x_val = float(input("Input the value of x : "))
if not(x[0] <= x_val <= x[x.size - 1]):
    print('The entered value is out of range to interpolate')
    sys.exit()

#Input the degree of the polynomial
x_degree = int(input("Input the degree of x : "))
if not(0 <= x_degree < x.size):
    print('The degree of the polynomial must be not negative and less than the number of x')
    sys.exit()

#Input the value y
y_val = float(input("Input the value of y : "))
if not(y[0] <= y_val <= y[y.size - 1]):
    print('The entered value is out of range to interpolate')
    sys.exit()

#Input the degree of the polynomial
y_degree = int(input("Input the degree of y : "))
if not(0 <= y_degree < y.size):
    print('The degree of the polynomial must be not negative and less than the number of y')
    sys.exit()

print()
result = computeBilinearInterpolation(x, y, z, x_degree, y_degree, x_val, y_val)
print("Result = {:.6g}".format(result))
print("f(x, y) = {:.6g}".format(f(x_val, y_val)))
print("Error = {:.6g}".format(fabs(result - f(x_val, y_val))))
