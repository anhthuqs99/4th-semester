from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys

from algorithms import *

class Line:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.scene_item = None


class Cutter:
    def __init__(self):
        self.coords = []
        self.scene_items = []
# Класс главного окна
class MyWindow(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)

        # Загрузка интерфейса
        uic.loadUi("design.ui", self)

        # Переменные
        self.bg_color = QColor(Qt.white)
        self.line_color = QColor(Qt.black)
        self.cutter_color = QColor(Qt.red)
        self.cut_line_color = QColor(Qt.green)
        self.highlighted_lines = []

        self.ctrl_pressed = False
        self.lines = []
        self.cur_line = []
        self.follow_line = None

        self.cutter = None
        self.drawing_cutter = False
        self.follow_cutter = None

        # Добавляем полотно
        self.scene = QGraphicsScene(0, 0, 1920, 1080)
        self.mainview.setScene(self.scene)
        self.pen = QPen()
        self.mainview.ensureVisible(0, 0, 0, 0)
        self.mainview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mainview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Элементы ввода в интерфейсе
        self.inputs = [
            self.but_add_line,
            self.but_add_cutter,
            self.but_end_cutter,
            self.but_choose_cutter,
            self.but_cut,
            self.but_clear,
            self.inp_x1,
            self.inp_x2,
            self.inp_y1,
            self.inp_y2,
            self.inp_x_cutter,
            self.inp_y_cutter,
        ]

        # Настройка полей ввода
        reg_ex = QRegExp("[0-9]+")
        int_validator = QRegExpValidator(reg_ex, self)
        self.inp_x1.setValidator(int_validator)
        self.inp_x2.setValidator(int_validator)
        self.inp_y1.setValidator(int_validator)
        self.inp_y2.setValidator(int_validator)
        self.inp_x_cutter.setValidator(int_validator)
        self.inp_x_cutter.setValidator(int_validator)

        # Привязка кнопок
        self.but_add_line.clicked.connect(lambda: get_line(self))
        self.but_add_cutter.clicked.connect(lambda: get_cutter(self))
        self.but_end_cutter.clicked.connect(lambda: end_cutter(self))
        self.but_choose_cutter.clicked.connect(lambda: choose_cutter(self))
        self.but_cut.clicked.connect(lambda: cut(self))
        self.but_clear.clicked.connect(lambda: clear(self))

        # Остальные настройки
        self.mainview.setMouseTracking(True)
        self.mainview.viewport().installEventFilter(self)

    # Отслеживание передвижения мыши
    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseMove and source is self.mainview.viewport():
            x = event.x()
            y = event.y()

            following_line(self, x, y)
            following_cutter(self, x, y)

        return QWidget.eventFilter(self, source, event)

    # Нажатие клавиши
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Control:
            self.ctrl_pressed = True

    # Отжатие клавиши
    def keyReleaseEvent(self, event):
        key = event.key()
        if key == Qt.Key_Control:
            self.ctrl_pressed = False

    # Нажатие кнопки мыши
    def mousePressEvent(self, event):
        but = event.button()
        x = event.x()
        y = event.y()

        borders = self.mainview.geometry().getCoords()
        if borders[0] <= x < borders[2] and borders[1] <= y < borders[3]:
            x -= borders[0]
            y -= borders[1]
        else:
            return

        if but == 1:
            line_on_screen(self, x, y)
            cutter_on_screen(self, x, y)
            remove_highlight(self)

        if but == 2:
            end_cutter_on_screen(self)


def get_line(self):
    try:
        x1 = int(self.inp_x1.text())
        y1 = int(self.inp_y1.text())
        x2 = int(self.inp_x2.text())
        y2 = int(self.inp_y2.text())
    except ValueError:
        mes("Неверные данные отрезка")
        return -1

    add_line(self, x1, y1, x2, y2, self.line_color)


def get_cutter(self):
    try:
        x = int(self.inp_x_cutter.text())
        y = int(self.inp_y_cutter.text())
    except ValueError:
        mes("Неверные данные отсекателя")
        return -1

    if self.drawing_cutter == False:
        del_cutter(self)
        remove_highlight(self)

    if not self.cutter:
        print("created cutter")
        self.cutter = Cutter()
        self.drawing_cutter = True

    self.cutter.coords.append((x, y))

    if len(self.cutter.coords) > 1:
        print("here")
        self.pen.setColor(self.cutter_color)
        c = self.cutter.coords
        self.cutter.scene_items.append(self.scene.addLine(c[-1][0], c[-1][1], c[-2][0], c[-2][1], self.pen))


def end_cutter(self):
    if self.drawing_cutter:
        self.pen.setColor(self.cutter_color)

        if len(self.cutter.coords) > 2:
            c = self.cutter.coords
            self.cutter.scene_items.append(self.scene.addLine(c[-1][0], c[-1][1], c[0][0], c[0][1], self.pen))

            self.drawing_cutter = False
            self.scene.removeItem(self.follow_cutter)


def choose_cutter(self):
    del_cutter(self)
    self.cutter = Cutter()
    self.drawing_cutter = True
    remove_highlight(self)


def cut(self):
    if self.cutter and len(self.cutter.coords) > 2:

        convex, clockwise = check_convex_polygon(self.cutter.coords)
        if convex == False:
            mes("Отсекатель невыпуклый")
            del_cutter(self)
            return -1

        remove_highlight(self)

        for i in range(len(self.lines)):
            p1 = [self.lines[i].x1, self.lines[i].y1]
            p2 = [self.lines[i].x2, self.lines[i].y2]
            
            visible, r1, r2 = cyrus_beck(self.cutter.coords, p1, p2, clockwise)

            if visible:
                highlight(self, r1, r2)

        redraw_cutter(self)
                
            

def clear(self):
    self.scene.clear()

    self.lines.clear()
    self.cur_line.clear()
    self.follow_line = None

    self.cutter = None
    self.follow_cutter = None
    self.drawing_cutter = False

# Выводит окно с предупреждением
def mes(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)

    msg.setWindowTitle("Внимание")
    msg.setText(text)

    msg.setStandardButtons(QMessageBox.Ok)

    retval = msg.exec_()


# Рисует отрезки
def add_line(self, x1, y1, x2, y2, color):
    self.pen.setColor(color)

    line = Line()

    line.x1 = x1
    line.y1 = y1
    line.x2 = x2
    line.y2 = y2
    line.scene_item = self.scene.addLine(x1, y1, x2, y2, self.pen)

    self.lines.append(line)


def redraw_cutter(self):
    if self.cutter:
        n = len(self.cutter.coords)

        for i in self.cutter.scene_items:
            self.scene.removeItem(i)
        self.cutter.scene_items.clear()

        self.pen.setColor(self.cutter_color)
        for i in range(n):
            p1 = self.cutter.coords[i - 1]
            p2 = self.cutter.coords[i]

            self.cutter.scene_items.append(self.scene.addLine(p1[0], p1[1], p2[0], p2[1], self.pen))


# OK
def del_cutter(self):
    if self.cutter:
        for c in self.cutter.scene_items:
            self.scene.removeItem(c)
        self.cutter = None


# OK Рисует отрезки
def line_on_screen(self, x, y):
    if not self.drawing_cutter:
        if self.ctrl_pressed == 0 or len(self.cur_line) == 0:
            self.cur_line.append((x, y))

        else:
            prev = self.cur_line[0]

            dx = x - prev[0]
            dy = y - prev[1]

            if abs(dy) >= abs(dx):
                self.cur_line.append((prev[0], y))
            else:
                self.cur_line.append((x, prev[1]))

        if len(self.cur_line) == 2:
            c1, c2 = self.cur_line
            add_line(self, c1[0], c1[1], c2[0], c2[1], self.line_color)
            self.cur_line.clear()
            self.scene.removeItem(self.follow_line)
            redraw_cutter(self)


def cutter_on_screen(self, x, y):
    if self.drawing_cutter:
        self.pen.setColor(self.cutter_color)

        c = self.cutter.coords

        if self.ctrl_pressed == 0 or len(c) == 0:
            c.append((x, y))

        else:
            prev = c[-1]

            dx = x - prev[0]
            dy = y - prev[1]

            if abs(dy) >= abs(dx):
                c.append((prev[0], y))
            else:
                c.append((x, prev[1]))

        if len(c) > 1:
            self.cutter.scene_items.append(self.scene.addLine(c[-1][0], c[-1][1], c[-2][0], c[-2][1], self.pen))


def end_cutter_on_screen(self):
    if self.drawing_cutter:
        self.pen.setColor(self.cutter_color)

        if len(self.cutter.coords) > 2:
            c = self.cutter.coords
            self.cutter.scene_items.append(self.scene.addLine(c[-1][0], c[-1][1], c[0][0], c[0][1], self.pen))

            self.drawing_cutter = False
            self.scene.removeItem(self.follow_cutter)



# OK
def following_line(self, x, y):
    if len(self.cur_line) == 1:
        prev = self.cur_line[0]
        self.pen.setColor(self.line_color)

        if self.follow_line:
            self.scene.removeItem(self.follow_line)

        if self.ctrl_pressed:
            dx = x - prev[0]
            dy = y - prev[1]

            if abs(dy) >= abs(dx):
                cur = (prev[0], y)
            else:
                cur = (x, prev[1])

            self.follow_line = self.scene.addLine(prev[0], prev[1], cur[0], cur[1], self.pen)
        else:
            self.follow_line = self.scene.addLine(prev[0], prev[1], x, y, self.pen)


def following_cutter(self, x, y):
    if self.drawing_cutter and len(self.cutter.coords) > 0:
        prev = self.cutter.coords[-1]
        self.pen.setColor(self.cutter_color)

        if self.follow_cutter:
            self.scene.removeItem(self.follow_cutter)

        if self.ctrl_pressed:
            dx = x - prev[0]
            dy = y - prev[1]

            if abs(dy) >= abs(dx):
                cur = (prev[0], y)
            else:
                cur = (x, prev[1])

            self.follow_cutter = self.scene.addLine(prev[0], prev[1], cur[0], cur[1], self.pen)
        else:
            self.follow_cutter = self.scene.addLine(prev[0], prev[1], x, y, self.pen)


# OK
def draw_line(self, dot1, dot2, color):
    self.pen.setColor(color)
    self.scene.addLine(dot1[0], dot1[1], dot2[0], dot2[1], self.pen)


def highlight(self, p1, p2):
    self.pen.setColor(self.cut_line_color)
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])

    for i in range(3):
        if dx > dy:
            line = self.scene.addLine(p1[0], p1[1] - 1 + i, p2[0], p2[1] - 1 + i, self.pen)
        else:
            line = self.scene.addLine(p1[0] - 1 + i, p1[1], p2[0] - 1 + i, p2[1], self.pen)

        self.highlighted_lines.append(line)


def remove_highlight(self):
    for i in self.highlighted_lines:
        self.scene.removeItem(i)
    self.highlighted_lines.clear()


if __name__ == '__main__':
    app = QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())