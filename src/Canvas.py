from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen, QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QSizePolicy


class Canvas(QWidget):

    def __init__(self, parent, brush):
        super().__init__(parent)
        self.image = QImage(800, 600, QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.last_point = QPoint()
        self.brush = brush

        self.setFixedHeight(600)
        self.setFixedWidth(800)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()
            print(self.last_point)

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(
                QPen(self.brush.brush_color, self.brush.brush_size, self.brush.line_type, self.brush.cap_type,
                     self.brush.join_type))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvas_painter = QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())
