from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from time import time

from scene import *
from weather import *

WIDTH = 800
HEIGHT = 600
Z_MIN = -300
global DX, DY, DZ
DX, DY, DZ = 20, 20, -10

root = Tk()
root.title("City weather")
root.geometry("1200x800")

def get_light():
    try:
        direction = int(Light_val.get())
        # exchange x and y 
        return vector(1, direction, 1)
    except: return vector(1, 1, 1)
def showImage(dx, dy, dz, light, canvas):
    with_shadow = int(Shadow_val.get())
    save_image(dx, dy, dz, light, with_shadow)
    img = ImageTk.PhotoImage(Image.open("result.png"))

    canvas.create_image((WIDTH/2, HEIGHT/2), image = img)
    canvas.grid(row = 0, column = 1)
    root.update()
    root.mainloop()
def btnShowClick(canvas):
    try:
        dx = int(MoveDxVar.get())
        dy = int(MoveDyVar.get())
        dz = int(MoveDzVar.get())
        light = get_light()
        showImage(dx, dy, dz, light, canvas)
        DX, DY, DZ = dx, dy, dz
    except ValueError:
        messagebox.showinfo("Error", "Value must be integer")

def btnStopCLick(canvas):
    img = ImageTk.PhotoImage(Image.open("result.png"))

    canvas.create_image((WIDTH/2, HEIGHT/2), image = img)
    canvas.grid(row = 0, column = 1)
    root.update()
    root.mainloop()

def btnFogClick(canvas):
    intensity = 1
    try:
        intensity = float(Fog_val.get())
    except ValueError: pass
    fog_color = (GRAY[0] * intensity, GRAY[1] * intensity, GRAY[2] * intensity)
    fog_image = Image.open("result.png")
    buf = rain_buf(DX, DY, DZ)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            cur_color = fog_image.getpixel((x, y))
            if buf[y][x] < Z_MIN:
                fog_image.putpixel((x, y), mix_color(GRAY, cur_color))
            else:
                inten =  1 - ((buf[y][x] + 400 // 2) / 400)
                if inten == -1:
                    inten = 0
                fog_image.putpixel((x, y), mix_color_intensive(fog_color, cur_color, inten))
    fog_image.save("fog_result.png")

    img = ImageTk.PhotoImage(Image.open("fog_result.png"))
    canvas.create_image((WIDTH/2, HEIGHT/2), image = img)
    canvas.grid(row = 0, column = 1)
    root.update()
    root.mainloop()
    return 

def btnRainCLick(canvas):
    intensity = 1
    try:
        intensity = float(Rain_val.get())
    except ValueError: pass
    print(intensity)
    rain_vertex = random_rain(int(5000 * intensity))
    buf = rain_buf(DX, DY, DZ)
    try:
        rain_direction = int(Light_val.get())
    except ValueError: rain_direction = 0

    for i in range(500):
        rain_image = Image.open("result.png")
        img_draw = ImageDraw.Draw(rain_image)
        for j in range(1000):
            x, y, z = rain_vertex[j][0], rain_vertex[j][1], rain_vertex[j][2]
            z_buf = -1000
            if (x > 0 and x < WIDTH and y > 0 and y < HEIGHT):
                z_buf = buf[y][x]
            x, y, z = rain_drop(x, y, z, rain_direction * 10, 10, 10, img_draw, z_buf)
            rain_vertex[j] = (x, y, z)

        rain_image.save("rain_result.png")
        rain_result_img = ImageTk.PhotoImage(Image.open("rain_result.png"))
        canvas.create_image((WIDTH/2, HEIGHT/2), image = rain_result_img)
        canvas.grid(row = 0, column = 1)
        root.update()
        # time.sleep(0.02)
    img = ImageTk.PhotoImage(Image.open("result.png"))

    canvas.create_image((WIDTH/2, HEIGHT/2), image = img)
    canvas.grid(row = 0, column = 1)
    root.update()
    root.mainloop()
    return 

def btnBothCLick(canvas):
    rain_vertex = random_rain(1000)
    buf = rain_buf(DX, DY, DZ)

    for i in range(500):
        rain_image = Image.open("fog_result.png")
        img_draw = ImageDraw.Draw(rain_image)
        for j in range(1000):
            x, y, z = rain_vertex[j][0], rain_vertex[j][1], rain_vertex[j][2]
            z_buf = -1000
            if (x > 0 and x < WIDTH and y > 0 and y < HEIGHT):
                z_buf = buf[y][x]
            x, y, z = rain_drop(x, y, z, 10, 10, 10, img_draw, z_buf)
            rain_vertex[j] = (x, y, z)

        rain_image.save("rain_result.png")
        rain_result_img = ImageTk.PhotoImage(Image.open("rain_result.png"))
        canvas.create_image((WIDTH/2, HEIGHT/2), image = rain_result_img)
        canvas.grid(row = 0, column = 1)
        root.update()
        # time.sleep(0.02)
    img = ImageTk.PhotoImage(Image.open("result.png"))

    canvas.create_image((WIDTH/2, HEIGHT/2), image = img)
    canvas.grid(row = 0, column = 1)
    root.update()
    root.mainloop()
    return 


def btnAddClick():
    return

def btnUpClick(canvas):
    global DX, DY, DZ
    DX -= 10
    light = get_light()
    showImage(DX, DY, DZ, light, canvas)

def btnDownClick():
    global DX, DY, DZ
    DX += 10
    light = get_light()
    showImage(DX, DY, DZ, light, canvas)

def btnRightClick():
    global DX, DY, DZ
    DY -= 10
    light = get_light()
    showImage(DX, DY, DZ, light, canvas)

def btnLeftClick():
    global DX, DY, DZ
    DY += 10
    light = get_light
    showImage(DX, DY, DZ, light, canvas)

Font = "Arial 13"
EntryW = 13

frame = Frame(root, width = 400)
canvas = Canvas(root, width = 800, height = 600, bg = "white")

insert = Frame(root, width = 400)
turn = Frame(root, width = 400)
weather = Frame(root, width = 400)

MoveDxVar = StringVar(value = "20")
MoveDyVar = StringVar(value = "20")
MoveDzVar = StringVar(value = "-10")

Label(frame, text = "Coordinates:", font = Font).grid(row = 0, column = 0)
# dx value
Label(frame, text = "dx:", font = Font).grid(row = 1, column = 0)
Entry(frame, width = EntryW, textvariable = MoveDxVar, font = Font).grid(row = 1, column = 1)
# dy value
Label(frame, text = "dy:", font = Font).grid(row = 1, column = 2)
Entry(frame, width = EntryW, textvariable = MoveDyVar, font = Font).grid(row = 1, column = 3)
# dz value
Label(frame, text = "dz:", font = Font).grid(row = 2, column = 0)
Entry(frame, width = EntryW, textvariable = MoveDzVar, font = Font).grid(row = 2, column = 1)
# btn show
Button(frame, text = "Show", command = lambda: btnShowClick(canvas), font = Font).grid(row = 2, column = 2, columnspan = 2)

#insert frame
#value insert
insertCenterXVar = StringVar(value = "0")
insertCenterZVar = StringVar(value = "0")
insertDxVar = StringVar(value = "0")
insertDzVar = StringVar(value = "0")
insertHVar = StringVar(value = "0")
#insert frame
Label(insert, text = "Scene:", font = Font).grid(row = 0, column = 0)
# x value
Label(insert, text = "Center x:", font = Font).grid(row = 1, column = 0)
Entry(insert, width = EntryW, textvariable = insertCenterXVar, font = Font).grid(row = 1, column = 1)
Label(insert, text = "dx:", font = Font).grid(row = 1, column = 2)
Entry(insert, width = EntryW, textvariable = insertDxVar, font = Font).grid(row = 1, column = 3)
# z value
Label(insert, text = "Center z:", font = Font).grid(row = 2, column = 0)
Entry(insert, width = EntryW, textvariable = insertCenterZVar, font = Font).grid(row = 2, column = 1)
Label(insert, text = "dz:", font = Font).grid(row = 2, column = 2)
Entry(insert, width = EntryW, textvariable = insertDzVar, font = Font).grid(row = 2, column = 3)
# h value
Label(insert, text = "Height:", font = Font).grid(row = 3, column = 0)
Entry(insert, width = EntryW, textvariable = insertHVar, font = Font).grid(row = 3, column = 1)
# btn add building
Button(insert, text = "   Add   ", command = lambda: btnAddClick(), font = Font).grid(row = 3, column = 2, columnspan = 2)

#turn frame
Label(turn, text = "Turn Option: ", font = Font).grid(row = 0, column = 0)
Button(turn, text = "   Up  ", command = lambda:btnUpClick(canvas), font = Font).grid(row = 1, column = 0, columnspan = 2)
Button(turn, text = "  Down ", command = lambda:btnDownClick(), font = Font).grid(row = 3, column = 0, columnspan = 2)
Button(turn, text = " Left  ", command = lambda:btnLeftClick(), font = Font).grid(row = 2, column = 0, columnspan = 1)
Button(turn, text = " Right ", command = lambda:btnRightClick(), font = Font).grid(row = 2, column = 1, columnspan = 1)

#weather frame
Light_val = IntVar()
Shadow_val = IntVar()
Rain_val = StringVar(value = "0.5")
Fog_val = StringVar(value = "0.5")

Label(weather, text = "Weather: ", font = Font).grid(row = 0, column = 0)
#rain
Button(weather, text = "   Rain  ", command = lambda:btnRainCLick(canvas), font = Font).grid(row = 1, column = 0, columnspan = 2)
Button(weather, text = "   Stop  ", command = lambda:btnStopCLick(canvas), font = Font).grid(row = 1, column = 2, columnspan = 2)
Label(weather, text = "Isty:", font = Font, width = 5).grid(row = 1, column = 4, columnspan = 1)
Entry(weather, width = 5, textvariable = Rain_val, font = Font).grid(row = 1, column = 5, columnspan = 1)

#Fog
Button(weather, text = "   Fog   ", command = lambda:btnFogClick(canvas), font = Font).grid(row = 2, column = 0, columnspan = 2)
Button(weather, text = "   Stop  ", command = lambda:btnStopCLick(canvas), font = Font).grid(row = 2, column = 2, columnspan = 2)
Label(weather, text = "Isty:", font = Font, width = 5).grid(row = 2, column = 4, columnspan = 1)
Entry(weather, width = 5, textvariable = Fog_val, font = Font).grid(row = 2, column = 5, columnspan = 1)
#Both rain and fog
Button(weather, text = "   Both  ", command = lambda:btnBothCLick(canvas), font = Font).grid(row = 3, column = 0, columnspan = 2)
Button(weather, text = "   Stop  ", command = lambda:btnStopCLick(canvas), font = Font).grid(row = 3, column = 2, columnspan = 2)
#Light
Checkbutton(weather, text = "Shadow", variable = Shadow_val, onvalue = 1, offvalue = 0, font = Font).grid(row = 5, column = 0, columnspan = 2)
Label(weather, text = "Light: ", font = Font).grid(row = 4, column = 0)
Radiobutton(weather, text = "left   ",variable = Light_val, value = 1, font = Font).grid(row = 6, column = 0, columnspan = 2)
Radiobutton(weather, text = "center ",variable = Light_val, value = 0, font = Font).grid(row = 7, column = 0, columnspan = 2)
Radiobutton(weather, text = "right  ",variable = Light_val, value = -1, font = Font).grid(row = 8, column = 0, columnspan = 2)

frame.grid(row = 0, column = 0)
insert.grid(row = 1, column = 0)
turn.grid(row = 2, column = 0)
weather.grid(row = 3, column = 0)
canvas.grid(row = 0, column = 1, rowspan = 5)

root.mainloop()