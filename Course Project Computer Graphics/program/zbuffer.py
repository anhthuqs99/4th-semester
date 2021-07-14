from math import *
from structures import * 

def init_buf(w, h, value):
    buf = [[value for j in range(w)] for i in range(h)]
    return buf

#update
def list_point_inside_polygon(vertexs, last_x = WIDTH, last_y = HEIGHT, first_x = 0, first_y = 0):
    n = len(vertexs)
    points = []
    for i in range(1, n - 1):
        ver = [vertexs[0], vertexs[i], vertexs[i + 1]]
        points.append(list_point_inside_triangle(ver, last_x, last_y, first_x, first_y))
    return points
def list_point_inside_triangle(vertexs, last_x, last_y, first_x, first_y):
    Points = []
    x = []
    y = []
    z = []
    for ver in vertexs:
        x.append(ver.x)
        y.append(ver.y)
        z.append(ver.z)
    yMax = max(y)
    yMin = min(y)

    if yMin < first_y:
        yMin = first_y
    if yMax > last_y:
        yMax = last_y

    x1, x2 = 0, 0
    z1, z2 = 0, 0


    for yDot in range(yMin, yMax + 1):
        fFirst = 1
        for n in range(-1, 2):
            if (yDot >= max(y[n], y[n + 1]) or yDot < min(y[n], y[n + 1])):
                continue
            m = (y[n] - yDot) / (y[n] - y[n + 1])
            if fFirst == 0:
                x2 = x[n] + m * (x[n + 1] - x[n])
                z2 = z[n] + m * (z[n + 1] - z[n])
            else:
                x1 = x[n] + m * (x[n + 1] - x[n])
                z1 = z[n] + m * (z[n + 1] - z[n])
            fFirst = 0
        if x2 < x1:
            x1, x2 = x2, x1
            z1, z2 = z2, z1
        x_Start = round(first_x) if x1 < first_x else round(x1)
        x_End = round(x2) if x2 < last_x else round(last_x)

        for xDot in range(x_Start, x_End):
            m = (x1 - xDot) / (x1 - x2)
            zDot = z1 + m * (z2 - z1)
            Points.append(vertex(round(xDot), round(yDot), round(zDot)))
    return Points

## Z-buffer using simple lighting
def get_color(surface, light, color):
    nor = get_normal(surface, len(surface))
    cos_al = abs(cos_vector(light, nor))
    # cos_al = cos_vector(light, nor)
    # if cos_al < 0:
    #     cos_al += 1
    I = [round(i * cos_al) for i in color]
    return I[0], I[1], I[2]

def z_buf_surface(image, buf, surface, color_light, w, h, last_x, last_y, first_x, first_y):
    points = list_point_inside_polygon(surface, last_x, last_y, first_x, first_y)
    for triangle in points:
        for ver in triangle:
            ver.x += WIDTH // 2
            ver.y += HEIGHT // 2 ## center
            if (ver.x < 0) or (ver.x >= w) or (ver.y < 0) or (ver.y >= h): #out of screen
                continue
            if ver.z > buf[ver.y][ver.x]:
                buf[ver.y][ver.x] = ver.z
                image.putpixel((ver.x, ver.y), color_light)
    return buf

def z_buffer_object(image, buf, surfaces, light, color, w, h, last_x, last_y, first_x, first_y):
    for sur in surfaces:
        color_light = get_color(sur, light, color)
        buf = z_buf_surface(image, buf, sur, color_light, w, h, last_x, last_y, first_x, first_y)
        # image.show()
    return buf
def shadow_z_buffer(image, objects, light, w, h):
    buf = init_buf(w, h, -HEIGHT)
    for obj in objects:

        # if change parameters here change the parameters in function shadow too
        obj.rotate(0, 0, 0, -10 * light.x, -10 * light.y, 10 * light.z)
        buf = z_buffer_object(image, buf, obj.polygons, light, obj.color, w, h, w, h, -w, -h)
    return buf
def z_buffer(image, objects, light, w, h):
    buf = init_buf(w, h, -HEIGHT)
    for obj in objects:
        buf = z_buffer_object(image, buf, obj.polygons, light, obj.color, w, h, w, h, -w, -h)
    # image.show()
    return buf

def mix_color(color1, color2):
    color = []
    for i in range(3):
        color.append(round((color1[i] + color2[i]) / 2))
    return color[0], color[1], color[2]
def shadow(image, image2, objects, objects2, light, w, h):
    depth_buf = z_buffer(image, objects, light, w, h)
    shadow_buf = shadow_z_buffer(image2, objects2, light, w, h)
    for xDot in range(w):
        for yDot in range(h):
            zDot = depth_buf[yDot][xDot]
            if (zDot != -HEIGHT): # z background
                # fixed
                # new_x, new_y, new_z = rotate_vertex(xDot, yDot, zDot, w // 2, h // 2, 0, -10, 10, 0) #rotate center
                new_x, new_y, new_z = rotate_vertex(xDot, yDot, zDot, w // 2, h // 2, 0, -10 * light.x, -10 * light.y, 10 * light.z)
                if new_x < 0 or new_x >= w or new_y < 0 or new_y >= h:
                    continue # out of screen
                z_shadow = shadow_buf[new_y][new_x]
                if new_z + 5  < z_shadow:
                    # image.putpixel((xDot, yDot), BLACK)
                    cur_color = image.getpixel((xDot, yDot))
                    image.putpixel((xDot, yDot), mix_color(cur_color, BLACK))
