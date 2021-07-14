from math import *
from time import time
from PyQt5.QtGui import QColor
from matplotlib import pyplot as plt

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
#ЦДА
def time_DDA(x1, y1, x2, y2):
    # points = []
    time_beg = time()

    lenx = (x2 - x1)
    leny = (y2 - y1)
    dx = abs(lenx)
    dy = abs(leny)
    step = int(max(dx, dy))

    x_inc = lenx / step
    y_inc = leny / step

    x, y = x1, y1

    for i in range(step + 1):
        x += x_inc
        y += y_inc
        round(x)
        round(y)

    # return points
    time_end = time()

    return time_end - time_beg
#
def time_br_float(x1, y1, x2, y2):
    # points = []
    time_beg = time()

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        return time() - time_beg

    x = x1
    y = y1

    sx = sign(dx)
    sy = sign(dy)

    dx = abs(dx)
    dy = abs(dy)

    if (dx > dy):
        change = 0
    else:
        change = 1
        dx, dy = dy, dx

    m = dy / dx
    e = m - 0.5

    while (x != x2) or (y != y2):
        if e >= 0:
            if change == 0:
                y += sy
            else:
                x += sx
            e -= 1
        if e < 0:
            if change == 0:
                x += sx
            else:
                y += sy
            e += m

    # return points
    time_end = time()
    
    return time_end - time_beg

def time_br_int(x1, y1, x2, y2):
    # points = []
    time_beg = time()

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        return points
    
    sx = sign(dx)
    sy = sign(dy)

    dx = abs(dx)
    dy = abs(dy)

    if (dx > dy):
        change = 0
    else:
        change = 1
        dx, dy = dy, dx

    e = 2 * dy - dx

    x, y = x1, y1

    while (x != x2) or (y != y2):
        if e >= 0:
            if change == 0:
                y += sy
            else:
                x += sx
            e -= 2 * dx
        else:
            if change == 0:
                x += sx
            else:
                y += sy
            e += 2 * dy
    # return points
    time_end = time()
    
    return time_end - time_beg

def time_br_smooth(x1, y1, x2, y2, fill, I):
    # points = []
    time_beg = time()
    grad = get_intensity("#000000", "#ffffff", 50000)
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        return time() - time_beg

    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    if (dy > dx):
        dx, dy = dy, dx
        change = 1
    else:
        change = 0
    try:
        tg = dy / dx * I
    except ZeroDivisionError:
        tg = 1
    e = I / 2
    w = I - tg
    x = x1
    y = y1

    while (x != x2) or (y != y2):
        if e >= w:
            y += sy
            x += sx
            e -= w
        else:
            if change == 0:
                x += sx
            else:
                y += sy
            e += tg

    # return points
    time_end = time()

    return time_end - time_beg

def time_wu(x1, y1, x2, y2, fill, I):
    # points = []
    time_beg = time()
    grad = get_intensity("#000000", "#ffffff", 70000)
    if x1 == x2 and y1 == y2: 
        return points

    steep = abs(y2 - y1) > abs(x2 - x1)

    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        tg = 1
    else: 
        tg = dy / dx
    #first end point
    xend = round(x1)
    yend = y1 + tg * (xend - x1)
    xpx1 = xend
    y = yend + tg

    #second end point
    xend = int(x2 + 0.5)
    xpx2 = xend
    
    if steep:
        for x in range(xpx1, xpx2):
            y += tg
    else:
        for x in range(xpx1, xpx2):
            y += tg

    # return points
    time_end = time()

    return time_end - time_beg

def get_intensity(line_color, bg_color, intensity):
    grad = []
    r1, g1, b1 = 0, 0 ,0
    r2, g2, b2 = 50, 50, 50
    r_ratio = float(r2 - r1) / intensity
    g_ratio = float(g2 - g1) / intensity
    b_ratio = float(b2 - b1) / intensity

    for i in range(intensity):
        nr = int(r1 + r_ratio * i)
        ng = int(g1 + g_ratio * i)
        nb = int(b1 + b_ratio * i)
        grad.append("#%4.4x%4.4x%4.4x" % (nr, ng, nb))

    # grad.reverse()

    return grad
def time_test(N):
    res = []
    x1 = 0
    y1 = 0
    x2 = x1 + N
    y2 = y1 + N
    # grad = get_rgb_intensity(self, self.color_line, self.color_bg, 100)
    grad = ["#fff" for i in range(100)]
    res.append(time_DDA(x1, y1, x2, y2))
    res.append(time_br_float(x1, y1, x2, y2))
    res.append(time_br_int(x1, y1, x2, y2))
    res.append(time_br_smooth(x1, y1, x2, y2, grad, 100))
    res.append(time_wu(x1, y1, x2, y2, grad, 100))

    name = ["ЦДА", "Б(Целые)", "Б(Действительные)", "Б(Без ступ)", "ВУ"]
    plt.xlabel("Алгоритм")
    plt.ylabel("Времия")
    plt.bar(name, res, width = 0.7,  color = 'blue')
    plt.show()
    return res

def stepping():
    x_axis = []
    y_axis = []

    for i in range(91):
        x_axis.append(i)
        if i < 45:
            y_axis.append(floor(100 * sin(i * pi / 180)))
        else:
            y_axis.append(floor(100) * cos(i * pi / 180))
    plt.plot(x_axis, y_axis)
    plt.xlabel("Угол")
    plt.ylabel("Количество ступения")
    plt.show()
