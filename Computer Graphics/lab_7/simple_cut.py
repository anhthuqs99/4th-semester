import copy
INFINITY = 1000000000000000000000000000000

#Вычисление сумм кодов концов отрезка
def count_S(T):
    return sum(T)

#Вычисление логического произведения кодов концов отрезка
def count_P(T1, T2):
    P = 0
    for i in range(len(T1)):
        P += (T1[i] * T2[i])
    return P

#Вычисление кодов концов отрезка
def count_T(p, xl, xr, yd, yu):
    x, y = p[0], p[1]
    # y = p[1]
    T = [0, 0, 0, 0]
    T[0] = 1 if x < xl else 0
    T[1] = 1 if x > xr else 0
    T[2] = 1 if y < yd else 0
    T[3] = 1 if y > yu else 0
    return T


def easy_cut(xl, xr, yd, yu, p1, p2):
    T1 = count_T(p1, xl, xr, yd, yu)
    T2 = count_T(p2, xl, xr, yd, yu)

    S1 = count_S(T1)
    S2 = count_S(T2)

    PR = 1 #признак видимости
    m = INFINITY  # тангенс

    Q = p1
    r1 = copy.deepcopy(p1)
    r2 = copy.deepcopy(p2)

    if (S1 == 0) and (S2 == 0):
        return show_pix(PR, r1, r2)

    P = count_P(T1, T2)
    if P != 0:
        PR = -1
        return show_pix(PR,r1, r2)

    if S1 == 0:
        r1 = copy.deepcopy(p1)
        Q = copy.deepcopy(p2)
        i = 2
        return CUT(PR, i, Q, p1, p2, r1, r2, xl, xr, yd, yu, False)

    if S2 == 0:
        r1 = copy.deepcopy(p2)
        Q = copy.deepcopy(p1)
        i = 2
        return CUT(PR, i, Q, p1, p2, r1, r2, xl, xr, yd, yu, False)

    i = 0
    return CUT(PR, i, Q, p1, p2, r1, r2, xl, xr, yd, yu)


def show_pix(PR, p1, p2):
    if PR == 1:
        return True, p1, p2
    else:
        return False, p1, p2


def CUT(PR, i, Q, p1, p2, r1, r2, xl, xr, yd, yu, flag=True):
    # Определение расположения отрезка
    if flag:
        i += 1
        if i > 2:
            return show_pix(PR, r1, r2)

        Q = p1 if i == 1 else p2 # Q = Pi

    if p1[0] == p2[0]:
        return CUT_skip(PR, i, Q, p1, p2, r1, r2, xl, xr, yd, yu, INFINITY)
    #Вычисление тангенса угла наклона отрезка
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])

    if Q[0] < xl:
        # Вычисление ординаты точки пересечения с левой границей отсекателя
        yp = m * (xl - Q[0]) + Q[1]

        # проверка корректности найденного пересечения 
        if yp >= yd and yp <= yu:
            if i == 1:
                r1[0] = xl
                r1[1] = yp
            else:
                r2[0] = xl
                r2[1] = yp
            return CUT(PR, i, Q, p1, p2, r1, r2, xl, xr, yd, yu)
        # else:
    if Q[0] > xr:
        # Вычисление ординаты точки пересечения с правой границей
        yp = m * (xr - Q[0]) + Q[1]
        # проверка корректности найденного пересечения
        if yp >= yd and yp <= yu:
            if i == 1:
                r1[0] = xr
                r1[1] = yp
            else:
                r2[0] = xr
                r2[1] = yp
            return CUT(PR, i, Q, p1, p2, r1, r2, xl, xr, yd, yu)

    return CUT_skip(PR, i, Q, p1, p2, r1, r2, xl, xr, yd, yu, m)

def CUT_skip(PR, i, Q, p1, p2, r1, r2, xl, xr, yd, yu, m):
    # проверка горизонтальности
    if m == 0:
        return CUT(PR, i, Q, p1, p2, r1, r2, xl, xr, yd, yu, m)
    
    if Q[1] > yu:
        # Вычисление абсциссы точки пересечения с верхней границей
        xp = (yu - Q[1]) / m + Q[0]
        #  Проверка корректности найденного пересечения
        if xp >= xl and xp <= xr:
            if i == 1:  
                r1[0] = xp
                r1[1] = yu
            else:
                r2[0] = xp
                r2[1] = yu
            return CUT(PR, i, Q, p1, p2, r1, r2, xl, xr, yd, yu)


    if Q[1] < yd:
        #  Вычисление абсциссы точки пересечения с нижней границей
        xp = (yd - Q[1]) / m + Q[0]
        # Проверка корректности найденного пересечения
        if xp >= xl and xp <= xr:
            if i == 1:
                r1[0] = xp
                r1[1] = yd
            else:
                r2[0] = xp
                r2[1] = yd
            return CUT(PR, i, Q, p1, p2, r1, r2, xl, xr, yd, yu)
    PR = -1
    return show_pix(PR, r1, r2)
