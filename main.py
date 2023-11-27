import sys
from random import randint
from PyQt5 import uic

from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QWidget
from UI import Ui_Form


class MyPillow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.objects = []
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter()
            painter.begin(self)
            for obj in self.objects:
                painter.setBrush(QColor(obj[3], obj[4], obj[5]))
                painter.drawEllipse(obj[0], obj[1], obj[2], obj[2])
            x, y, r = randint(1, 700), randint(1, 400), randint(1, 300)
            self.draw_ellipse(painter, x, y, r)
            painter.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_ellipse(self, painter, x, y, rad):
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        painter.setBrush(QColor(r, g, b))
        self.objects.append((x, y, rad, r, g, b))
        painter.drawEllipse(x, y, rad, rad)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
