from math import cos, sin, pi, sqrt


# Place pix on x, y
def draw_pix(self, x, y):
    self.canvas.create_line(x, y, x+1, y+1, fill=self.color_pen)
    return 0


# ==========CIRCLES==========
def draw_circle_canon(self, xc, yc, r):
    for x in range(0, r + 1, 1):
        y = round(sqrt(r ** 2 - x ** 2))

        draw_pix(self, xc + x, yc + y)
        draw_pix(self, xc + x, yc - y)
        draw_pix(self, xc - x, yc + y)
        draw_pix(self, xc - x, yc - y)
    for y in range(0, r + 1, 1):
        x = round(sqrt(r ** 2 - y ** 2))

        draw_pix(self, xc + x, yc + y)
        draw_pix(self, xc + x, yc - y)
        draw_pix(self, xc - x, yc + y)
        draw_pix(self, xc - x, yc - y)
    return 0


def draw_circle_param(self, xc, yc, r):
    len = round(pi * r / 2)

    for i in range(0, len + 1, 1):
        x = round(r * cos(i / r))
        y = round(r * sin(i / r))

        draw_pix(self, xc + x, yc + y)
        draw_pix(self, xc + x, yc - y)
        draw_pix(self, xc - x, yc + y)
        draw_pix(self, xc - x, yc - y)

    return 0


def draw_circle_br(self, xc, yc, r):
    x = 0  # задание начальных значений
    y = r
    d = 2 * (1 - r)  # значение D(x,y)  при (0,R)

    while y >= 0:
        # высвечивание текущего пиксела
        draw_pix(self, xc + x, yc + y)
        draw_pix(self, xc + x, yc - y)
        draw_pix(self, xc - x, yc + y)
        draw_pix(self, xc - x, yc - y)

        if d < 0:  # пиксель лежит внутри окружности
            d1 = 2 * (d + y) - 1
            x += 1

            if d1 <= 0:  # горизонтальный шаг
                d = d + 2 * x + 1
            else:  # диагональный шаг
                y -= 1
                d = d + 2 * (x - y + 1)

            continue

        if d > 0:  # пиксель лежит вне окружности
            d2 = 2 * (d - x) - 1
            y -= 1

            if d2 > 0:  # вертикальный шаг
                d = d - 2 * y + 1
            else:  # диагональный шаг
                x += 1
                d = d + 2 * (x - y + 1)

            continue

        if d == 0:  # пиксель лежит на окружности
            x += 1  # диагональный шаг
            y -= 1
            d = d + 2 * (x - y + 1)

    return 0


def draw_circle_mid(self, xc, yc, r):
    x = 0  # начальные значения
    y = r
    p = 5 / 4 - r  # (x + 1)^2 + (y - 1/2)^2 - r^2

    while True:
        draw_pix(self, xc + x, yc + y)
        draw_pix(self, xc + x, yc - y)
        draw_pix(self, xc - x, yc + y)
        draw_pix(self, xc - x, yc - y)

        draw_pix(self, xc + y, yc + x)
        draw_pix(self, xc + y, yc - x)
        draw_pix(self, xc - y, yc + x)
        draw_pix(self, xc - y, yc - x)

        x += 1

        if p < 0:  # средняя точка внутри окружности, ближе верхний пиксел, горизонтальный шаг
            p += 2 * x + 1
        else:  # средняя точка вне окружности, ближе диагональный пиксел, диагональный шаг
            y -= 1
            p += 2 * (x - y) + 1

        if x > y:
            break

    return 0


def draw_circle_std(self, xc, yc, r):
    self.canvas.create_oval(xc-r, yc-r, xc+r, yc+r, outline=self.color_pen)

    return 0

# ==========ELLIPSES==========
def draw_ellipse_canon(self, xc, yc, a, b):
    for x in range(0, a + 1, 1):
        y = round(b * sqrt(1 - (x/a)**2))

        draw_pix(self, xc + x, yc + y)
        draw_pix(self, xc + x, yc - y)
        draw_pix(self, xc - x, yc + y)
        draw_pix(self, xc - x, yc - y)

    return 0


def draw_ellipse_param(self, xc, yc, a, b):
    m = max(a, b)
    len = round(pi * m / 2)

    for i in range(0, len + 1, 1):
        x = round(a * cos(i / m))
        y = round(b * sin(i / m))

        draw_pix(self, xc + x, yc + y)
        draw_pix(self, xc + x, yc - y)
        draw_pix(self, xc - x, yc + y)
        draw_pix(self, xc - x, yc - y)

    return 0


def draw_ellipse_br(self, xc, yc, a, b):
    dot = []
    x = 0  # начальные значения
    y = b
    a2 = a ** 2
    b2 = b ** 2
    d = round(b2 / 2 - 2 * a2 * b + a2 / 2)

    while y >= 0:
        draw_pix(self, xc + x, yc + y)
        draw_pix(self, xc + x, yc - y)
        draw_pix(self, xc - x, yc + y)
        draw_pix(self, xc - x, yc - y)
        
        if d < 0:  # пиксель лежит внутри эллипса
            d1 = 2 * (d + a2 * y) - a2
            x += 1
            if d1 <= 0:  # горизотальный шаг
                d = d + 2 * b2 * x + b2
            else:  # диагональный шаг
                y -= 1
                d = d + 2 * (b2 * x -  a2 * y )+ a2 + b2

            continue

        if d > 0:  # пиксель лежит вне эллипса
            d2 = 2 * (d - b2 * x) - b2
            y -= 1

            if d2 > 0:  # вертикальный шаг
                d = d - 2 * a2 * y + a2
            else:  # диагональный шаг
                x += 1
                d = d + 2 * (b2 * x - a2 * y) + a2 + b2

            continue

        if d == 0:  # пиксель лежит на окружности
            x += 1  # диагональный шаг
            y -= 1
            d = d + 2 * (b2 * x - a2 * y) + a2 + b2

    return 0


def draw_ellipse_mid(self, xc, yc, a, b):
    x = 0  # начальные положения
    y = b
    a2 = a ** 2
    b2 = b ** 2
    p = b2 - a2 * b + 0.25 * a2  # начальное значение параметра принятия решения в области tg<1
    while 2 * b2 * x < 2 * a2 * y:  # пока тангенс угла наклона меньше 1
        draw_pix(self, xc + x, yc + y)
        draw_pix(self, xc + x, yc - y)
        draw_pix(self, xc - x, yc + y)
        draw_pix(self, xc - x, yc - y)

        x += 1

        if p < 0:  # средняя точка внутри эллипса, ближе верхний пиксел, горизонтальный шаг
            p += 2 * b2 * x + b2
        else:  # средняя точка вне эллипса, ближе диагональный пиксел, диагональный шаг
            y -= 1
            p += 2 * b2 * x - 2 * a2 * y + b2

    p = b2 * (x + 0.5) ** 2 + a2 * (y - 1) ** 2 - a2 * b2
    # начальное значение параметра принятия решения в области tg>1 в точке (х + 0.5, y - 1) полседнего положения

    while y >= 0:
        draw_pix(self, xc + x, yc + y)
        draw_pix(self, xc + x, yc - y)
        draw_pix(self, xc - x, yc + y)
        draw_pix(self, xc - x, yc - y)

        y -= 1

        if p > 0:
            p -= 2 * a2 * y + a2
        else:
            x += 1
            p += 2 * b2 * x - 2 * a2 * y + a2

    return 0


def draw_ellipse_std(self, xc, yc, a, b):
    self.canvas.create_oval(xc - a, yc - b, xc + a, yc + b, outline=self.color_pen)

    return 0
