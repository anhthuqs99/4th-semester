from math import *

def rotateX(x, y, z, teta):
    teta = teta * pi / 180
    # buf = y
    newy = cos(teta) * y - sin(teta) * z
    newz = cos(teta) * z + sin(teta) * y
    return x, newy, newz

def rotateY(x, y, z, teta):
    teta = teta * pi / 180
    # buf = x
    newx = cos(teta) * x + sin(teta) * z
    newz = cos(teta) * z - sin(teta) * x
    return newx, y, newz

def rotateZ(x, y, z, teta):
    teta = teta * pi / 180
    # buf = x
    newx = cos(teta) * x - sin(teta) * y
    newy = cos(teta) * y + sin(teta) * x
    return newx, newy, z

def rotate_vertex(x, y, z, xc, yc, zc, tetaX, tetaY, tetaZ):
    x, y, z = x - xc, y - yc, z - zc
    x, y, z = rotateZ(x, y, z, tetaZ)
    x, y, z = rotateX(x, y, z, tetaX)
    x, y, z = rotateY(x, y, z, tetaY)
    return round(x + xc), round(y + yc), round(z + zc)