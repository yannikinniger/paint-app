import sys

from PyQt5.QtWidgets import QApplication

from src.DrawWindow import DrawWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    window = DrawWindow(screen_resolution)
    window.show()
    app.exec()
