import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Git и случайные окружности')
        self.btn = QPushButton('Сделай круг', self)
        self.btn.resize(120, 40)
        self.btn.move(180, 40)
        self.painting = False
        self.btn.clicked.connect(self.do)

    def do(self):
        self.painting = True
        self.repaint()

    def paintEvent(self, event):
        if self.painting:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()

    def drawing(selfself, qp):
        size = random.randint(10, 50)
        x, y = random.randint(10, 450), random.randint(65, 450)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(x, y, size, size)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = Window()
    wd.show()
    sys.exit(app.exec())
