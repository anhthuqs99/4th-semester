from math import ceil
from random import randint
def get_edges(dots_mas):
    edges = []

    for dots in dots_mas:
        for i in range(len(dots)):
            if i + 1 > len(dots) - 1:
                edges.append([dots[i][0], dots[i][1], dots[0][0],dots[0][1]])
            else:
                edges.append([dots[i][0], dots[i][1], dots[i + 1][0], dots[i+1][1]])
    return edges

def get_intersections(edges):
    intersections = []

    for i in range(len(edges)):
        x1 = edges[i][0]
        y1 = edges[i][1]
        x2 = edges[i][2]
        y2 = edges[i][3]

        len_x = abs(ceil(x2) - ceil(x1))
        len_y = abs(ceil(y2) - ceil(y1))

        if len_y != 0:
            dx = ((x2 > x1) - (x2 < x1)) * len_x / len_y
            dy = ((y2 > y1) - (y2 < y1))

            x1 += dx / 2
            y1 += dy / 2

            for j in range(len_y):
                intersections.append((ceil(x1), ceil(y1)))
                x1 += dx
                y1 += dy

    return intersections

def find_max_x(edges):
    # x_max = 0
    # for i in range(len(edges)):
    #     if edges[i][0] > x_max:
    #         x_max = edges[i][0]
    #     if edges[i][2] > x_max:
    #         x_max = edges[i][2]
    # return x_max
    index = randint(0, len(edges) - 1)
    return edges[-1][0]

def fill_figure(self, inter, x_max):
    bg_color = self.winfo_rgb(self.bg_color)
    fill_color = self.winfo_rgb(self.fill_color)
    bd_color = self.winfo_rgb(self.bd_color)
    color = fill_color
    self.canvas.create_line(x_max, 0, x_max, 600, fill = self.bd_color)

    # for i in range(len(inter) - 1, 0, -1):
    for i in range(len(inter)):
        x, y = inter[i][0], inter[i][1]
        self.image.putpixel((x, y), bd_color)

        if x > x_max:
            step = -1
        else: step = 1
            # x, x_max = x_max, x

        for x_draw in range(x , x_max, step):
            col = self.image.getpixel((x_draw, y))
            col = "#%02x%02x%02x" % (col[0], col[1], col[2])
            if col == self.bg_color:
                self.pen = self.fill_color
                color = fill_color
            elif col == self.fill_color:
                self.pen = self.bg_color
                color = self.bd_color
            elif col == self.bd_color:
                self.pen = self.bd_color
                color = bd_color
            self.canvas.create_line(x_draw, y, x_draw + step, y, fill = self.pen)
            self.image.putpixel((x_draw, y), color)
    return 
def draw_image(self, inter):
    bd_color = self.winfo_rgb(self.bd_color)
    for point in inter:
        x, y = point[0], point[1]
        self.image.putpixel((x, y), bd_color)

def fill_figure_delay(self, inter, x_max):
    bg_color = self.winfo_rgb(self.bg_color)
    fill_color = self.winfo_rgb(self.fill_color)
    bd_color = self.winfo_rgb(self.bd_color)
    color = fill_color
    
    self.canvas.create_line(x_max, 0, x_max, 600, fill = self.bd_color)

    x, y = inter.pop()
    self.image.putpixel((x, y), bd_color)

    if x > x_max:
        step = -1
    else: step = 1
        # x, x_max = x_max, x

    for x_draw in range(x , x_max + step, step):
        col = self.image.getpixel((x_draw, y))
        col = "#%02x%02x%02x" % (col[0], col[1], col[2])
        if col == self.bg_color:
            self.pen = self.fill_color
            color = fill_color
        elif col == self.fill_color:
            self.pen = self.bg_color
            color = bg_color
        elif col == self.bd_color:
            self.pen = self.bd_color
            color = bd_color
        self.canvas.create_line(x_draw, y, x_draw + step, y, fill = self.pen)
        self.image.putpixel((x_draw, y), color)
    # self.canvas.create_line(x, y, x + 1, y, fill = self.bd_color)
    if len(inter) > 0:
        self.canvas.after(self.delay, lambda:fill_figure_delay(self, inter, x_max))
    return 
    
