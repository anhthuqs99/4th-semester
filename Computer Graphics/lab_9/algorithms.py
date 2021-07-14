from main import *
def sign(x):
    if not x:
        return 0
    else:
        return x / abs(x)

# Проверка выпукности
def isConvex(edges):
    flag = 1

    # начальные вершины
    vo = edges[0]  # iая вершина
    vi = edges[1]  # i+1 вершина
    vn = edges[2]  # i+2 вершина и все остальные

    x1 = vi.x() - vo.x()
    y1 = vi.y() - vo.y()

    x2 = vn.x() - vi.x()
    y2 = vn.y() - vi.y()

    # определяем знак ординаты
    r = x1 * y2 - x2 * y1
    prev = sign(r)

    for i in range(2, len(edges) - 1):
        if not flag:
            break
        vo = edges[i - 1]
        vi = edges[i]
        vn = edges[i + 1]

        x1 = vi.x() - vo.x()
        y1 = vi.y() - vo.y()

        x2 = vn.x() - vi.x()
        y2 = vn.y() - vi.y()

        r = x1 * y2 - x2 * y1
        curr = sign(r)

        # если знак предыдущей координаты не совпадает, то возможно многоугольник невыпуклый
        if curr != prev:
            flag = 0
        prev = curr

    # проверить последнюю с первой вершины
    vo = edges[len(edges) - 1]
    vi = edges[0]
    vn = edges[1]

    x1 = vi.x() - vo.x()
    y1 = vi.y() - vo.y()

    x2 = vn.x() - vi.x()
    y2 = vn.y() - vi.y()

    r = x1 * y2 - x2 * y1
    curr = sign(r)
    if curr != prev:
        flag = 0

    return flag * curr

# Найти пересечение
def is_intersection(ed1, ed2, norm):
    vis1 = is_visiable(ed1[0], ed2[0], ed2[1], norm)
    vis2 = is_visiable(ed1[1], ed2[0], ed2[1], norm)
    if (vis1 and not vis2) or (not vis1 and vis2):

        p1 = ed1[0]
        p2 = ed1[1]

        q1 = ed2[0]
        q2 = ed2[1]

        delta = (p2.x() - p1.x()) * (q1.y() - q2.y()) - (q1.x() - q2.x()) * (p2.y() - p1.y())
        delta_t = (q1.x() - p1.x()) * (q1.y() - q2.y()) - (q1.x() - q2.x()) * (q1.y() - p1.y())

        if abs(delta) <= 1e-6:
            return p2

        t = delta_t / delta

        I = QPointF()
        I.setX(ed1[0].x() + (ed1[1].x() - ed1[0].x()) * t)
        I.setY(ed1[0].y() + (ed1[1].y() - ed1[0].y()) * t)
        return I
    else:
        return False

# Проверка видимости вершины
def is_visiable(point, peak1, peak2, norm):
    v = vec_mul([point, peak1], [peak2, peak1])
    if norm * v < 0:
        return True
    else:
        return False

#Векторное произведение
def vec_mul(v1, v2):
    x1 = v1[0].x() - v1[1].x()
    y1 = v1[0].y() - v1[1].y()

    x2 = v2[0].x() - v2[1].x()
    y2 = v2[0].y() - v2[1].y()

    return x1 * y2 - x2 * y1


# Алгоритм Сазерленда-Ходжмена
def sutherland_hodgman(C, P, norm):
    Nc = len(C)
    Np = len(P)
    C.append(C[0]) # добавить начальную вершину отсекателя в конец

    s = None
    f = None
    
    for i in range(Nc): # цикл по вершинам отсекателя
        Q = []  # результирующий массив
        for j in range(Np):    # цикл по вершинам многоугольника
            if j == 0: # первая вершина
                f = P[j]
            else:
                t = is_intersection([s, P[j]], [C[i], C[i + 1]], norm)
                if t:
                    Q.append(t)

            s = P[j]
            # Проверка видимости вершины S относительно ребра CiCi+1
            if is_visiable(s,  C[i], C[i + 1], norm):
                    Q.append(s)
        # Проверка ненулевого количества вершин в результирующем массиве
        if len(Q) == 0:
            continue

        t = is_intersection([s, f], [C[i], C[i + 1]], norm)
        if t:
            Q.append(t)

        P = copy.deepcopy(Q)
        Np = len(P)

    # if len(P) == 0:
    if Np == 0:
        return False
    else:
        return QPolygonF(P)
