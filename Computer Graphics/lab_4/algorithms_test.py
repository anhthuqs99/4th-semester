from math import cos, sin, pi, sqrt
from time import time


# ==========CIRCLES TEST==========
def test_circle_canon(xc, yc, r):
    time_beg = time()
    for x in range(0, r + 1, 1):
        y = round(sqrt(r ** 2 - x ** 2))

        pix_x = xc + x; pix_y = yc + y
        pix_x = xc + x; pix_y = yc - y
        pix_x = xc - x; pix_y = yc + y
        pix_x = xc - x; pix_y = yc - y

    for y in range(0, r + 1, 1):
        x = round(sqrt(r ** 2 - y ** 2))

        pix_x = xc + x; pix_y = yc + y
        pix_x = xc + x; pix_y = yc - y
        pix_x = xc - x; pix_y = yc + y
        pix_x = xc - x; pix_y = yc - y

    time_end = time()
    return time_end - time_beg


def test_circle_param(xc, yc, r):
    time_beg = time()

    len = round(pi * r / 2)
    if len == 0:
        return -1

    for i in range(0, len + 1, 1):
        x = round(r * cos(i / r))
        y = round(r * sin(i / r))

        pix_x = xc + x; pix_y = yc + y
        pix_x = xc + x; pix_y = yc - y
        pix_x = xc - x; pix_y = yc + y
        pix_x = xc - x; pix_y = yc - y
    time_end = time()

    return time_end - time_beg


def test_circle_br(xc, yc, r):
    time_beg = time()

    x = 0
    y = r
    d = 2 - 2 * r

    while y >= 0:
        pix_x = xc + x; pix_y = yc + y
        pix_x = xc + x; pix_y = yc - y
        pix_x = xc - x; pix_y = yc + y
        pix_x = xc - x; pix_y = yc - y

        if d < 0:
            buf = 2 * d + 2 * y - 1
            x += 1

            if buf <= 0:
                d = d + 2 * x + 1
            else:
                y -= 1
                d = d + 2 * x - 2 * y + 2

            continue

        if d > 0:
            buf = 2 * d - 2 * x - 1
            y -= 1

            if buf > 0:
                d = d - 2 * y + 1
            else:
                x += 1
                d = d + 2 * x - 2 * y + 2

            continue

        if d == 0.0:
            x += 1
            y -= 1
            d = d + 2 * x - 2 * y + 2
    time_end = time()

    return time_end - time_beg

def test_circle_mid(xc, yc, r):
    time_beg = time()

    x = 0
    y = r
    p = 5 / 4 - r

    while True:
        pix_x = xc + x; pix_y = yc + y
        pix_x = xc + x; pix_y = yc - y
        pix_x = xc - x; pix_y = yc + y
        pix_x = xc - x; pix_y = yc - y
        x += 1

        if p < 0:
            p += 2 * x + 1
        else:
            p += 2 * x - 2 * y + 5
            y -= 1

        if x > y:
            break
    time_end = time()

    return time_end - time_beg

def test_circle_std(xc, yc, r):
    time_beg = time()
    for i in range (r):
        pix_x = xc - r; pix_y = yc - r
        # pix_x = xc + r; pix_y = yc + r
    time_end = time()
    
    return time_end - time_beg