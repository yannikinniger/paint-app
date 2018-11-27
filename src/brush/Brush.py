from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class Brush:
    """
    Contains all information needed to draw with a QPen
    Uses the Observer pattern, so it broadcasts all changes to it's Observables
    """

    def __init__(self):
        self._observers = set()
        self._brush_size = 3
        self._brush_color = QColor(Qt.black)
        self._line_type = Qt.SolidLine
        self._join_type = Qt.RoundJoin
        self._cap_type = Qt.RoundCap

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update_brush()

    @property
    def brush_size(self):
        return self._brush_size

    @brush_size.setter
    def brush_size(self, new_size):
        self._brush_size = new_size
        self._notify()

    @property
    def brush_color(self):
        return self._brush_color

    @brush_color.setter
    def brush_color(self, new_color):
        self._brush_color = new_color
        self._notify()

    @property
    def line_type(self):
        return self._line_type

    @line_type.setter
    def line_type(self, new_line_type):
        self._line_type = new_line_type
        self._notify()

    @property
    def join_type(self):
        return self._join_type

    @join_type.setter
    def join_type(self, new_join_type):
        self._join_type = new_join_type
        self._notify()

    @property
    def cap_type(self):
        return self._cap_type

    @cap_type.setter
    def cap_type(self, new_cap_type):
        self._cap_type = new_cap_type
        self._notify()
