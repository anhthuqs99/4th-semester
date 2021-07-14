from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap, QPainter, QTransform, QPolygonF
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPointF
import copy

from algorithms import *

red = Qt.red
green = Qt.green
black = Qt.black
now = None


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("design.ui", self)
        self.scene = Scene(0, 0, 561, 581)
        self.scene.win = self
        self.view.setScene(self.scene)
        self.poly.clicked.connect(lambda : set_pol(self))
        self.erase.clicked.connect(lambda: clean_all(self))
        self.paint.clicked.connect(lambda: clipping(self))
        self.rect.clicked.connect(lambda: set_rect(self))
        self.ect.clicked.connect(lambda: add_bars(self))
        self.lock.clicked.connect(lambda: lock(self))
        self.clip = []
        self.pol = []
        self.point_now_clip = None
        self.point_now_pol = None
        self.point_lock_pol = None
        self.point_lock_clip = None
        self.input_pol = False
        self.input_clip = False
        self.pen = QPen(black)


class Scene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, event):
        add_point(event.scenePos())

    def mouseMoveEvent(self, event):
        global w
        x = event.scenePos().x()
        y = event.scenePos().y()
        w.x.setText("{0}".format(x))
        w.y.setText("{0}".format(y))


def set_pol(win):
    if win.input_pol:
        win.input_pol = False
        win.rect.setDisabled(False)
        win.erase.setDisabled(False)
        win.paint.setDisabled(False)
        win.ect.setDisabled(False)
    else:
        win.input_pol = True
        win.rect.setDisabled(True)
        win.erase.setDisabled(True)
        win.paint.setDisabled(True)
        win.ect.setDisabled(True)


def set_rect(win):
    if win.input_clip:
        win.input_clip = False
        win.poly.setDisabled(False)
        win.erase.setDisabled(False)
        win.paint.setDisabled(False)
        win.ect.setDisabled(False)
    else:
        win.input_clip = True
        win.poly.setDisabled(True)
        win.erase.setDisabled(True)
        win.paint.setDisabled(True)
        win.ect.setDisabled(True)


def add_point(point):
    global w
    if w.input_clip:
        w.pen.setColor(black)
        if w.point_now_clip is None:
            w.point_now_clip = point
            w.point_lock_clip = point
            add_row(w.table_rect)
            i = w.table_rect.rowCount() - 1
            item_x = QTableWidgetItem("{0}".format(point.x()))
            item_y = QTableWidgetItem("{0}".format(point.y()))
            w.table_rect.setItem(i, 0, item_x)
            w.table_rect.setItem(i, 1, item_y)
        else:
            w.clip.append(point)
            w.point_now_clip = point
            add_row(w.table_rect)
            i = w.table_rect.rowCount() - 1
            item_x = QTableWidgetItem("{0}".format(point.x()))
            item_y = QTableWidgetItem("{0}".format(point.y()))
            w.table_rect.setItem(i, 0, item_x)
            w.table_rect.setItem(i, 1, item_y)
            item_x = w.table_rect.item(i-1, 0)
            item_y = w.table_rect.item(i-1, 1)
            w.scene.addLine(point.x(), point.y(), float(item_x.text()), float(item_y.text()), w.pen)

    if w.input_pol:
        w.pen.setColor(green)
        if w.point_now_pol is None:
            w.point_now_pol = point
            w.point_lock_pol = point
            add_row(w.table_pol)
            i = w.table_pol.rowCount() - 1
            item_x = QTableWidgetItem("{0}".format(point.x()))
            item_y = QTableWidgetItem("{0}".format(point.y()))
            w.table_pol.setItem(i, 0, item_x)
            w.table_pol.setItem(i, 1, item_y)
        else:
            w.pol.append(point)
            w.point_now_pol = point
            add_row(w.table_pol)
            i = w.table_pol.rowCount() - 1
            item_x = QTableWidgetItem("{0}".format(point.x()))
            item_y = QTableWidgetItem("{0}".format(point.y()))
            w.table_pol.setItem(i, 0, item_x)
            w.table_pol.setItem(i, 1, item_y)
            item_x = w.table_pol.item(i-1, 0)
            item_y = w.table_pol.item(i-1, 1)
            w.scene.addLine(point.x(), point.y(), float(item_x.text()), float(item_y.text()), w.pen)


def lock(win):
    if w.input_pol:
        win.pol.append(win.point_lock_pol)
        win.scene.addLine(win.point_now_pol.x(), win.point_now_pol.y(), win.point_lock_pol.x(), win.point_lock_pol.y(), w.pen)
        win.point_now_pol = None

    if w.input_clip:
        win.clip.append(win.point_lock_clip)
        win.scene.addLine(win.point_now_clip.x(), win.point_now_clip.y(), win.point_lock_clip.x(), win.point_lock_clip.y(), w.pen)
        win.point_now_clip = None


def add_row(win_table):
    win_table.insertRow(win_table.rowCount())


def clean_all(win):
    win.scene.clear()
    win.table_rect.clear()
    win.table_pol.clear()
    win.clip = []
    win.pol = []
    win.point_now_clip = None
    win.point_now_pol = None
    win.point_lock_clip = None
    win.point_lock_pol = None
    r = win.table_rect.rowCount()
    for i in range(r, -1, -1):
        win.table_rect.removeRow(i)

    r = win.table_pol.rowCount()
    for i in range(r, -1, -1):
        win.table_pol.removeRow(i)

def clipping(win):
    if len(win.clip) <= 1:
        QMessageBox.warning(win, "Ошибка!", "Отсекатель не задан!")

    if len(win.pol) <= 1:
        QMessageBox.warning(win, "Ошибка!", "Многоугольник не задан!")

    if len(win.pol) > 1 and len(win.clip) > 1:
        norm = isConvex(win.clip)
        if not norm:
            QMessageBox.warning(win, "Ошибка!", "Отсекатель не выпуклый!Операция не может быть проведена!")
        else:
            p = sutherland_hodgman(win.clip, win.pol, norm)
            if p:
                win.pen.setWidth(2)
                win.pen.setColor(red)
                win.scene.addPolygon(p, win.pen)
                win.pen.setWidth(1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())