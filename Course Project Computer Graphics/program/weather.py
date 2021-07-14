from structures import * 
from zbuffer import * 
from scene import * 
from PIL import * 
from PIL import Image, ImageDraw
from random import randint

def mix_color_intensive(color1, color2, inten):
    color = []
    for i in range(3):
        color.append(round((color1[i]  * inten + color2[i] ) / (inten + 1)))
    return color[0], color[1], color[2]

def rain_buf(dx, dy, dz):
    obj3 = create_cube_with_roof(250, 100, -100, 120, 100, 50, RED)
    obj2 = create_cube_with_roof(150, 60, 50, 60, 60, 60, BLUE)
    obj1 = creat_cube(0, 50, 0, 50, 50, 50, RED)
    ground = creat_cube(0, 0, 0, 400, 1,300, GREEN)
    objects = [obj1, obj2, obj3, ground]
    objects = get_scene_rotate(objects, dx, dy, dz)
    image = Image.new("RGB", (WIDTH, HEIGHT), "#ffffff")

    buf = z_buffer(image, objects, LIGHT, WIDTH, HEIGHT)
    for i in range(HEIGHT):
        buf[i].reverse()
    buf.reverse()
    return buf

def random_rain(MAX_N):
    rain_vertex = []
    for i in range(MAX_N):
        rain_vertex.append((randint(-1000, 1000), randint(-round(10000000 / MAX_N), round(10000000 / MAX_N)), randint(-100, 1000)))
    return rain_vertex

def rain_drop(x, y, z, dx, dy, dz, img_draw, z_buf):
    if (x > 0 and x < WIDTH and y > 0 and y < HEIGHT // 2 and z > z_buf and z_buf > -1000):
        img_draw.line((x , y, x + dx, y + dy), fill = RAIN_COLOR)
    x += dx
    y += dy
    return x, y, z



