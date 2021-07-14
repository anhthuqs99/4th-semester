from math import *
from PyQt5.QtGui import QColor

width_line = 1 #constant

def draw_pix(self, x, y, color):
    self.canvas.create_line(x, y, x + 1, y + 1,fill = color, width = width_line)
    return 0

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def fpart(x):
    return x - int(x)

def rpart(x):
    return 1 - fpart(x)

#ЦДА
def drawline_dda(self, x1, y1, x2, y2):
    # my code

    # lenx = int(x2 - x1)
    # leny = int(y2 - y1)
    lenx = x2 - x1
    leny = y2 - y1
    dx = abs(lenx)
    dy = abs(leny)
    step = max(dx, dy)

    x_inc = lenx / step
    y_inc = leny / step

    x, y = x1, y1

    for i in range(step + 1):
        draw_pix(self, round(x), round(y), self.color_pen)
        x += x_inc
        y += y_inc

    return 0
#
def drawline_br_float(self, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        draw_pix(self, x1, x1, self.color_pen)
        return 1

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
        draw_pix(self, x, y, self.color_pen)
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

    return 0

def drawline_br_int(self, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        draw_pix(self, x1, y1, self.color_pen)
        return 1
    
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
        draw_pix(self, x, y, self.color_pen)
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
    return 0

def drawline_br_smooth(self, x1, y1, x2, y2, fill, I):

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        draw_pix(self, x1, y1, self.color_pen)
        return 1

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
        draw_pix(self, x, y, fill[round(e) - 1])
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

    return 0
def drawline_wu(self, x1, y1, x2, y2, fill, I):
    if x1 == x2 and y1 == y2: 
        draw_pix(self, x1, y1, self.color_pen)

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
            self.canvas.create_line(int(y), x, int(y) + 1, int(x) + 2, fill = fill[int((I - 1) * abs(1 - y + int(y)))])
            self.canvas.create_line(int(y) + 1, int(x) + 1, int(y) + 2, int(x) + 2, fill = fill[int((I - 1) * abs(y - int(y)))])

            y += tg
    else:
        for x in range(xpx1, xpx2):
            self.canvas.create_line(int(x) + 1, int(y), int(x) + 2, int(y) + 1, fill = fill[round((I - 1) * abs(1 - y + floor(y)))])
            self.canvas.create_line(int(x) + 1, int(y) + 1, int(x) + 2, int(y) + 2, fill = fill[round((I - 1) * abs(y - floor(y)))])

            y += tg

def get_rgb_intensity(self, line_color, bg_color, intensity):
    grad = []
    (r1, g1, b1) = self.winfo_rgb(line_color) #get tuple of color of line
    (r2, g2, b2) = self.winfo_rgb(bg_color) #get tuple of color of background
    r_ratio = float(r2 - r1) / intensity
    g_ratio = float(g2 - g1) / intensity
    b_ratio = float(b2 - b1) / intensity

    for i in range(intensity):
        nr = int(r1 + r_ratio * i)
        ng = int(g1 + g_ratio * i)
        nb = int(b1 + b_ratio * i)
        grad.append("#%4.4x%4.4x%4.4x" % (nr, ng, nb))

    grad.reverse()

    return grad

def drawline_lib(self, x1, y1, x2, y2):
    self.canvas.create_line(x1, y1, x2 + 1, y2 + 1, fill = self.color_pen, width = width_line)
    return 0