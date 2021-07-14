#Проверка на выпукность
def check_convex_polygon(c):
    neg = 0
    pos = 0
    zer = 0

    for i in range(len(c)):
        c1 = c[i]
        c2 = c[(i + 1) % len(c)]
        c3 = c[(i + 2) % len(c)]

        vec1 = (c2[0] - c1[0], c2[1] - c1[1])
        vec2 = (c3[0] - c2[0], c3[1] - c2[1])
        
        res = vec1[0] * vec2[1] - vec1[1] * vec2[0]

        if res > 0:
            pos += 1    
        elif res < 0:
            neg += 1
        else:
            zer += 1

    if len(c) == zer:
        return False, None
    elif len(c) == pos + zer:
        return True, True
    elif len(c) == neg + zer:
        return True, False
    else:
        return False, None
# Вектор Нормали
def get_normal_vector(vec, clockwise):
    if clockwise:
        return (-vec[1], vec[0]) # по часовой стрелке
    else:
        return (vec[1], -vec[0]) # против часовой стрелки
# Вектор
def get_vec(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

# Скалярное произведение
def mul_scal(a, b):
    return a[0] * b[0] + a[1] * b[1]

# P(t) = P1 + (P2 - P1)t
def P(t, p1, p2):
    return (p1[0] + round((p2[0] - p1[0]) * t), p1[1] + round((p2[1] - p1[1]) * t))

# Алгоритм Кируса Бека
def cyrus_beck(cutter, p1, p2, clockwise):
    K = len(cutter)
    visible = False
    t_bot, t_top = 0, 1
    p_top, p_top = p1, p2
    D = get_vec(p1, p2)

    for i in range(K):
        # Вектор ребра
        edge_vec = get_vec(cutter[i], cutter[(i + 1) % K])
        # Вектор Нормали
        n_vec = get_normal_vector(edge_vec, clockwise)

        W = get_vec(cutter[i], p1)
        Dsc = mul_scal(D, n_vec)
        Wsc = mul_scal(W, n_vec)

        if Dsc == 0:
            if Wsc < 0:
                return visible, p1, p2
        else:
            t = -Wsc / Dsc
    
            if Dsc > 0:
                if t > 1:
                    return visible, p1, p2
                else:
                    t_bot = max(t_bot, t)
            else:
                if t < 0:
                    return visible, p1, p2
                else:
                    t_top = min(t_top, t)

    if t_bot <= t_top:
        p_bot = P(t_bot, p1, p2) # P(t_botton)
        p_top = P(t_top, p1, p2) # P(t_top)
        visible = True

    return visible, p_bot, p_top

