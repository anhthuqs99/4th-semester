from math import floor

# Returns edges from list of dots
def get_edges(dots_mas):
    edges = []

    for dots in dots_mas:
        for i in range(len(dots)):
            if i + 1 > len(dots) - 1:
                edges.append([dots[i][0], dots[i][1], dots[0][0],dots[0][1]])
            else:
                edges.append([dots[i][0], dots[i][1], dots[i + 1][0], dots[i+1][1]])
    
    # print(edges)

    # faster:
    #edges = [[dots_mas[i][j], dots_mas[i][0]] if j + 1 > len(dots_mas[i]) - 1 else [dots_mas[i][j], dots_mas[i][j + 1]] for i in range(len(dots_mas)) for j in range(len(dots_mas[i]))]

    return edges

def get_intersections(edges):
    intersections = []

    for i in range(len(edges)):
        x1 = edges[i][0]
        y1 = edges[i][1]
        x2 = edges[i][2]
        y2 = edges[i][3]

        len_x = abs(int(x2) - int(x1))
        len_y = abs(int(y2) - int(y1))

        if len_y != 0:
            dx = ((x2 > x1) - (x2 < x1)) * len_x / len_y
            dy = ((y2 > y1) - (y2 < y1))

            x1 += dx / 2
            y1 += dy / 2

            for j in range(len_y):
                intersections.append((int(x1), int(y1)))
                x1 += dx
                y1 += dy
    # print(intersections)
    return intersections


# def fill_figure(self, inter, x_max):

#     # for i in range(len(inter)):
#     # (x, y) = inter[i][0], inter[i][1]
#     (x, y) = inter.pop()

#     col = self.image.getpixel((x, y))
#     col = "#%02x%02x%02x" % (col[0], col[1], col[2])
#     if col == self.bg_color:
#         print(x, y, "change bg color")
#         self.pen = self.fill_color
#     # elif col == self.fill_color:
#     else:
#         print(x, y, "change fill color")
#         self.pen = self.bg_color
#     self.canvas.create_line(x + 1, y, x_max, y, fill = self.pen)
#     color = self.winfo_rgb(self.pen)
#     for x_draw in range(x, x_max + 1):
#         self.image.putpixel((x_draw, y), color)
#     if len(inter) > 0:
#         self.canvas.after(self.delay, lambda: fill_figure(self, inter, x_max))

def fill_figure(self, inter, x_max):
    # (x, y) = inter.pop()
    bg_color = self.winfo_rgb(self.bg_color)
    for i in range(len(inter)):
        x, y = inter[i][0], inter[i][1]
        if x > x_max:
            x, x_max = x_max + 2, x
        self.image.putpixel((x, y), bg_color)
        for x_draw in range(x, x_max):
            col = self.image.getpixel((x_draw, y))
            col = "#%02x%02x%02x" % (col[0], col[1], col[2])
            if col == self.bg_color:
                self.pen = self.fill_color
            # else:
            elif col == self.fill_color:
                self.pen = self.bg_color
            # if col != self.bd_color:
            # self.canvas.create_line(x_draw, y, x_draw + 1, y, fill = self.pen)
            color = self.winfo_rgb(self.pen)
            self.image.putpixel((x_draw, y), color)
        # if len(inter) > 0:
        # self.canvas.after(self.delay, lambda: fill_figure(self, inter, x_max))


def fill_figure_delay(self, inter, x_max):
    (x, y) = inter.pop()
    # if x > x_max:
    #     x, x_max = x_max, x

    for x_draw in range(x, x_max):
        col = self.image.getpixel((x_draw, y))
        col = "#%02x%02x%02x" % (col[0], col[1], col[2])
        if col == self.bg_color:
            self.pen = self.fill_color
        # else:
        elif col == self.fill_color:
            self.pen = self.bg_color
        # if col != self.bd_color:
        self.canvas.create_line(x_draw, y, x_draw + 1, y, fill = self.pen)
        color = self.winfo_rgb(self.pen)
        self.image.putpixel((x_draw, y), color)
    if len(inter) > 0:
        self.canvas.after(self.delay, lambda: fill_figure(self, inter, x_max))

def find_max_x(edges):
    # x_max = 0
    # for i in range(len(edges)):
    #     if edges[i][0] > x_max:
    #         x_max = edges[i][0]

    #     if edges[i][2] > x_max:
    #         x_max = edges[i][2]

    # return x_max
    return edges[len(edges) - 1][0]

