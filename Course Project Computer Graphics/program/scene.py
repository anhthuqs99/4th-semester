from structures import * 
from zbuffer import *
from PIL import *
from PIL import Image
from time import time

LIGHT = vector(0, 0, 1) #define

def creat_cube(xc, yc, zc, dx, dy, dz, color):
    p0 = vertex(xc - dx, yc - dy, zc - dz)
    p1 = vertex(xc - dx, yc - dy, zc + dz)
    p2 = vertex(xc + dx, yc - dy, zc - dz)
    p3 = vertex(xc - dx, yc + dy, zc - dz)
    p4 = vertex(xc + dx, yc + dy, zc + dz)
    p5 = vertex(xc - dx, yc + dy, zc + dz)
    p6 = vertex(xc + dx, yc - dy, zc + dz)
    p7 = vertex(xc + dx, yc + dy, zc - dz)

    sur1 = [p0, p2, p7, p3]
    sur2 = [p0, p1, p6, p2]
    sur3 = [p0, p3, p5, p1]
    sur4 = [p1, p6, p4, p5]
    sur5 = [p3, p5, p4, p7]
    sur6 = [p2, p7, p4, p6]

    cube = [sur1, sur2, sur3, sur4, sur5, sur6]

    return object(cube, [0, 0, 0], color)

def create_cube_with_roof(xc, yc, zc, dx, dy, dz, color):
    p0 = vertex(xc - dx, yc - dy, zc - dz)
    p1 = vertex(xc - dx, yc - dy, zc + dz)
    p2 = vertex(xc + dx, yc - dy, zc - dz)
    p3 = vertex(xc - dx, yc + dy, zc - dz)
    p4 = vertex(xc + dx, yc + dy, zc + dz)
    p5 = vertex(xc - dx, yc + dy, zc + dz)
    p6 = vertex(xc + dx, yc - dy, zc + dz)
    p7 = vertex(xc + dx, yc + dy, zc - dz)
    p8 = vertex(xc, yc + dy * 1.5,  zc)

    sur1 = [p0, p2, p7, p3]
    sur2 = [p0, p1, p6, p2]
    sur3 = [p0, p3, p5, p1]
    sur4 = [p1, p6, p4, p5]
    # sur5 = [p3, p5, p4, p7]
    sur5 = [p2, p7, p4, p6]
    sur6 = [p3, p7, p8]
    sur7 = [p7, p4, p8]
    sur8 = [p4, p5, p8]
    sur9 = [p5, p3, p8]

    cube = [sur1, sur2, sur3, sur4, sur5, sur6, sur7, sur8, sur9]

    return object(cube, [0, 0, 0], color)

def get_scene_rotate(objects, tetaX, tetaY, tetaZ):
    for obj in objects:
        obj.rotate(0, 0, 0, tetaX, tetaY, tetaZ)
    return objects

def save_image(dx, dy, dz, LIGHT, with_shadow = True):
    obj3 = create_cube_with_roof(250, 100, -100, 120, 100, 50, RED)
    obj2 = create_cube_with_roof(150, 60, 50, 60, 60, 60, BLUE)
    obj1 = creat_cube(0, 50, 0, 50, 50, 50, RED)
    ground = creat_cube(0, 0, 0, 400, 1,300, GREEN)

    objects = [obj1, obj2, obj3, ground]
    objects2 = [obj1, obj2, obj3]

    # objects = [obj1, obj2, ground]
    # objects2 = [obj1, obj2]
    objects = get_scene_rotate(objects, dx, dy, dz)
    # LIGHT = vector(-1, 1, -1)
        
    image = Image.new("RGB", (WIDTH, HEIGHT), "#ffffff")
    image2 = Image.new("RGB", (WIDTH, HEIGHT), "#ffffff")

    # time_begin = time()
    if with_shadow:
        shadow(image, image2, objects, objects2, LIGHT, WIDTH, HEIGHT)
    else:
        z_buffer(image, objects, LIGHT, WIDTH, HEIGHT)
    
    # time_end = time()
    # print("time zbuff: ", time_end - time_begin)

    # time_begin = time()
    
    # shadow(image, image2, objects, objects2, LIGHT, WIDTH, HEIGHT)
    
    # time_end = time()
    # print("time zbuff with shadow", time_end - time_begin)

    image = image.rotate(180)
    image.save("result.png")