from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
import sys

from simple_cut import *

class Line:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.scene_item = None


class Cutter:
    def __init__(self):
        self.x_left = 0
        self.y_up = 0
        self.x_right = 0
        self.y_down = 0
        self.scene_item = None
        
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

        self.ctrl_pressed = False
        self.lines = []
        self.cur_line = []
        self.follow_line = None

        self.cutter = None
        self.drawing_cutter = False
        self.cur_cutter = []
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
            self.but_choose_cutter,
            self.but_cut,
            self.but_clear,
            self.inp_x1,
            self.inp_x2,
            self.inp_y1,
            self.inp_y2,
            self.inp_x_left,
            self.inp_x_right,
            self.inp_y_up,
            self.inp_y_down
        ]

        # Настройка полей ввода
        reg_ex = QRegExp("[0-9]+")
        int_validator = QRegExpValidator(reg_ex, self)
        self.inp_x1.setValidator(int_validator)
        self.inp_x2.setValidator(int_validator)
        self.inp_y1.setValidator(int_validator)
        self.inp_y2.setValidator(int_validator)
        self.inp_x_left.setValidator(int_validator)
        self.inp_x_right.setValidator(int_validator)
        self.inp_y_up.setValidator(int_validator)
        self.inp_y_down.setValidator(int_validator)

        # Привязка кнопок
        self.but_add_line.clicked.connect(lambda: get_line(self))
        self.but_add_cutter.clicked.connect(lambda: get_cutter(self))
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
        x_left = int(self.inp_x_left.text())
        y_up = int(self.inp_y_up.text())
        x_right = int(self.inp_x_right.text())
        y_down = int(self.inp_y_down.text())
    except ValueError:
        mes("Неверные данные отрезка")
        return -1

    del_cutter(self)
    add_cutter(self, x_left, y_up, x_right, y_down, self.cutter_color)


def choose_cutter(self):
    del_cutter(self)
    self.drawing_cutter = True


def cut(self):
    if self.cutter:
        for i in range(len(self.lines)):
            xl = self.cutter.x_left
            xr = self.cutter.x_right
            yd = self.cutter.y_down
            yu = self.cutter.y_up
            p1 = [self.lines[i].x1, self.lines[i].y1]
            p2 = [self.lines[i].x2, self.lines[i].y2]
            yu, yd = yd, yu

            visible, p1, p2 = easy_cut(xl, xr, yd, yu, p1, p2)
            if visible:
                draw_line(self, p1, p2, self.cut_line_color)


def clear(self):
    self.scene.clear()

    self.lines.clear()
    self.cur_line.clear()
    self.follow_line = None

    self.cutter = None
    self.cur_cutter.clear()
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


def add_line(self, x1, y1, x2, y2, color):
    self.pen.setColor(color)

    line = Line()

    line.x1 = x1
    line.y1 = y1
    line.x2 = x2
    line.y2 = y2
    line.scene_item = self.scene.addLine(x1, y1, x2, y2, self.pen)

    self.lines.append(line)


def add_cutter(self, x_l, y_u, x_r, y_d, color):
    self.pen.setColor(color)

    if x_l > x_r:
        x_l, x_r = x_r, x_l
    if y_u > y_d:
        y_u, y_d = y_d, y_u

    cutter = Cutter()

    cutter.x_left = x_l
    cutter.y_up = y_u
    cutter.x_right = x_r
    cutter.y_down = y_d
    cutter.scene_item = self.scene.addRect(x_l, y_u, x_r - x_l, y_d - y_u, self.pen)

    self.cutter = cutter


def del_cutter(self):
    if self.cutter:
        self.scene.removeItem(self.cutter.scene_item)
    self.cutter = None


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


def cutter_on_screen(self, x, y):
    if self.drawing_cutter:
        if len(self.cur_cutter) < 2:
            self.cur_cutter.append((x, y))

        if len(self.cur_cutter) == 2:
            c1, c2 = self.cur_cutter
            add_cutter(self, c1[0], c1[1], c2[0], c2[1], self.cutter_color)
            self.cur_cutter.clear()
            self.scene.removeItem(self.follow_cutter)
            self.drawing_cutter = False


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
    if len(self.cur_cutter) == 1:
        x_l, y_u = self.cur_cutter[0]
        x_r, y_d = x, y
        self.pen.setColor(self.cutter_color)

        if self.follow_cutter:
            self.scene.removeItem(self.follow_cutter)

        if x_l > x_r:
            x_l, x_r = x_r, x_l
        if y_u > y_d:
            y_u, y_d = y_d, y_u

        self.follow_cutter = self.scene.addRect(x_l, y_u, x_r - x_l, y_d - y_u, self.pen)


def draw_line(self, dot1, dot2, color):
    self.pen.setColor(color)

    self.scene.addLine(dot1[0], dot1[1], dot2[0], dot2[1], self.pen)


if __name__ == '__main__':
    app = QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())