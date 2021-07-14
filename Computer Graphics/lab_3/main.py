import tkinter as tk 
import tkinter.ttk as ttk
from tkinter import messagebox 
from tkinter.colorchooser import askcolor
from matplotlib import pyplot as plt

from algorithms import *
from time_testing import *
from typing import NamedTuple

class Line(NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int
    color : str
    alg: int

class Spectrum(NamedTuple):
    x: int
    y: int
    r: int
    angle: int
    color: str
    alg: int
# App class
class Kg4App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)

        options_size = 336 # const
        can_x = args[0] - options_size
        can_y = args[1]

        tk.Tk.title(self, "Lab_03")
        tk.Tk.geometry(self, str(can_x + options_size) + "x" + str(can_y))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainPage, GraphPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.color_bg = "#fff"
        self.color_line = "#000000"

        self.color_pen = self.color_line
        self.objects = []
        self.res = []
        
        # TABS
        self.work = tk.Frame(self)
        self.tab_parent = ttk.Notebook(self.work, height=140)
        
        self.tab1 = ttk.Frame(self.tab_parent)
        self.tab2 = ttk.Frame(self.tab_parent)

        self.tab_parent.add(self.tab1, text="Линия")
        self.tab_parent.add(self.tab2, text="Спектр")
        self.tab_parent.grid(row=0, column=0, columnspan=2)

        #Variable Tab1
        self.var1_1 = tk.StringVar()
        self.var2_1 = tk.StringVar()
        self.var3_1 = tk.StringVar()
        self.var4_1 = tk.StringVar()
        #Variable Tab2
        self.var1_2 = tk.StringVar()
        self.var2_2 = tk.StringVar()
        self.var3_2 = tk.StringVar()
        self.var4_2 = tk.StringVar()

        # Tab 1
        self.e_w = 20
        self.tab1_label_1 = ttk.Label(self.tab1, text="X1:").grid(row=0, column=0)
        self.tab1_label_2 = ttk.Label(self.tab1, text="   Y1:").grid(row=0, column=2)
        self.tab1_label_3 = ttk.Label(self.tab1, text="X2:").grid(row=1, column=0)
        self.tab1_label_4 = ttk.Label(self.tab1, text="   Y2:").grid(row=1, column=2)
        self.tab1_entry_x1 = ttk.Entry(self.tab1, textvariable=self.var1_1, width=self.e_w).grid(row=0, column=1)
        self.tab1_entry_y1 = ttk.Entry(self.tab1, textvariable=self.var2_1, width=self.e_w).grid(row=0, column=3)
        self.tab1_entry_x2 = ttk.Entry(self.tab1, textvariable=self.var3_1, width=self.e_w).grid(row=1, column=1)
        self.tab1_entry_y2 = ttk.Entry(self.tab1, textvariable=self.var4_1, width=self.e_w).grid(row=1, column=3)
        self.tab1.grid_rowconfigure(0, weight=1)
        self.tab1.grid_rowconfigure(1, weight=1)
        self.tab1.grid_columnconfigure(0, weight=1)
        self.tab1.grid_columnconfigure(1, weight=1)

        # Tab 2
        self.tab2_label_1 = ttk.Label(self.tab2, text="X:").grid(row=0, column=0)
        self.tab2_label_2 = ttk.Label(self.tab2, text="   Y:").grid(row=0, column=2)
        self.tab2_label_3 = ttk.Label(self.tab2, text="L").grid(row=1, column=0)
        self.tab2_label_4 = ttk.Label(self.tab2, text="Angle:").grid(row=1, column=2)
        self.tab2_entry_x = ttk.Entry(self.tab2, textvariable=self.var1_2, width=self.e_w).grid(row=0, column=1)
        self.tab2_entry_y = ttk.Entry(self.tab2, textvariable=self.var2_2, width=self.e_w).grid(row=0, column=3)
        self.tab2_entry_a = ttk.Entry(self.tab2, textvariable=self.var3_2, width=self.e_w).grid(row=1, column=1)
        self.tab2_entry_b = ttk.Entry(self.tab2, textvariable=self.var4_2, width=self.e_w).grid(row=1, column=3)
        self.tab2.grid_rowconfigure(0, weight=1)
        self.tab2.grid_rowconfigure(1, weight=1)
        self.tab2.grid_columnconfigure(0, weight=1)
        self.tab2.grid_columnconfigure(1, weight=1)

        self.button_line_color = ttk.Button(self.work, text="Цвет линии",
                                            command=lambda: get_color_line(self)).grid(row=1, column=0)
        self.label_line_color = tk.Label(self.work, bg=self.color_line, width=20)
        self.label_line_color.grid(row=1, column=1)
        self.button_bg_color = ttk.Button(self.work, text="Цвет фона",
                                          command=lambda: get_color_bg(self)).grid(row=2, column=0)
        self.label_bg_color = tk.Label(self.work, bg=self.color_bg, width=20)
        self.label_bg_color.grid(row=2, column=1)

        self.ch_var = tk.IntVar()
        self.ch_button_color = ttk.Checkbutton(self.work, text="Рисовать цветом фона", variable=self.ch_var)
        self.ch_var.set(0)
        self.ch_button_color.grid(row=3, column=0)

        self.list_alg = ["ЦДА", "Брезенхема(Целые)", "Брезенхема(Действительные)",
                    "Брезенхема(Без ступенчатности)", "Алгоритм ВУ", "Библиотичный метод"]
        self.combobox_alg = ttk.Combobox(self.work, width=25, values=self.list_alg, state="readonly")
        self.combobox_alg.current(0)
        self.combobox_alg.grid(row=4, column=0)
        self.button_test = ttk.Button(self.work, text="Времия",
                                 command=lambda: time_test(100000)).grid(row=5, column=0)
        self.button_stepping = ttk.Button(self.work, text = 'Ступенчатность', 
                                command = lambda:stepping()).grid(row = 5, column = 1)
        self.button_draw = ttk.Button(self.work, text="Нарисовать",
                                 command=lambda: draw(self)).grid(row=6, column=0)
        self.button_clear = ttk.Button(self.work, text="Очистить",
                                  command=lambda: clear(self) ).grid(row = 6, column=1)
        self.work.pack(side=tk.RIGHT)
        self.canvas = tk.Canvas(self, bg=self.color_bg)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand = True)
        
# Graph page class
class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text="Вернуться",
                             command=lambda: controller.show_frame(MainPage))
        button1.pack()
def clear(self):
    self.canvas.delete("all")
    self.canvas.configure(bg=self.color_bg)

def mes(text):
    messagebox.showinfo("Внимание", text)

def get_color_line(self):
    color = askcolor()[1]

    if color:
        self.color_line = color
        self.label_line_color.configure(bg = color)

def get_color_bg(self):
    color = askcolor()[1]
    
    if color:
        self.color_bg = color
        self.label_bg_color.configure(bg = color)

        self.canvas.configure(bg = self.color_bg)

def draw(self):
    tab = self.tab_parent.index(self.tab_parent.select())

    if tab == 0:
        try:
            x1 = int(self.var1_1.get())
            y1 = int(self.var2_1.get())
            x2 = int(self.var3_1.get())
            y2 = int(self.var4_1.get())
        except ValueError:
            mes("Неверные данные")
            return -1

    if tab == 1:
        try:
            x = int(self.var1_2.get())
            y = int(self.var2_2.get())
            r = int(self.var3_2.get())
            angle = int(self.var4_2.get())
        except ValueError:
            mes("Неверные данные")
            return -1

    if int(self.ch_var.get()) == 1:
        color = self.color_bg
    else:
        color = self.color_line
    
    alg = self.combobox_alg.current()

    can_x = self.canvas.winfo_width()
    can_y = self.canvas.winfo_height()

    if tab == 0:
        line = Line(x1, y1, x2, y2, color, alg)
        draw_func(self, line)
    
    if tab == 1:
        spectrum = Spectrum(x, y, r, angle, color, alg)
        draw_func(self, spectrum)

def draw_spectrum(self, x0, y0, r, angle, alg, color):
    grad = get_rgb_intensity(self, self.color_line, self.color_bg, INTENSITY)

    step = int(360 / angle)
    for i in range(step):
        cur = (angle * pi / 180) * i
        # cur += ang
        x = int(round(x0 + r * cos(cur)))
        y = int(round(y0 + r * sin(cur)))

        if alg == 0:
            drawline_dda(self, x0, y0, x, y)
        elif alg == 1:
            drawline_br_float(self, x0, y0, x, y)
        elif alg == 2:
            drawline_br_int(self, x0, y0, x, y)
        elif alg == 3:
            drawline_br_smooth(self, x0, y0, x, y, grad, INTENSITY)
        elif alg == 4:
            drawline_wu(self, x0, y0, x, y, grad, INTENSITY) 
        elif alg == 5:
            drawline_lib(self, x0, y0, x, y)
INTENSITY = 100
def draw_func(self, obj):
    self.color_pen = obj.color
    grad = get_rgb_intensity(self, self.color_line, self.color_bg, INTENSITY)

    if type(obj) == Line:
        if obj.alg == 0:
            drawline_dda(self, obj.x1, obj.y1, obj.x2, obj.y2)
        elif obj.alg == 1:
            drawline_br_float(self, obj.x1, obj.y1, obj.x2, obj.y2)
        elif obj.alg == 2:
            drawline_br_int(self, obj.x1, obj.y1, obj.x2, obj.y2)
        elif obj.alg == 3:
            drawline_br_smooth(self, obj.x1, obj.y1, obj.x2, obj.y2, grad, INTENSITY)
        elif obj.alg == 4:
            drawline_wu(self, obj.x1, obj.y1, obj.x2, obj.y2, grad, INTENSITY)
        elif obj.alg == 5:
            drawline_lib(self, obj.x1, obj.y1, obj.x2, obj.y2)
    elif type(obj) == Spectrum: 
        draw_spectrum(self, obj.x, obj.y, obj.r, obj.angle, obj.alg, obj.color)
        

        
if __name__ == '__main__':
    app = Kg4App(1000, 600)
    app.mainloop()
