from PyQt5.QtWidgets import QVBoxLayout, QWidget, QGridLayout, QSizePolicy

from src.menus.brush_menus.BrushTypePicker import BrushTypePicker
from src.menus.brush_menus.ColorPicker import ColorPicker
from src.menus.brush_menus.SizePicker import SizePicker


class DrawMenu(QWidget):
    """
    Combines all the brush menus in a widget and layouts them
    """

    def __init__(self, window, brush):
        super().__init__(window)

        self.brush = brush
        self.layout = QVBoxLayout()
        self.color_picker = ColorPicker(brush)
        self.size_picker = SizePicker(brush)
        self.brush_type_picker = BrushTypePicker(brush)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.__layout()

    def __layout(self):
        self.layout = QGridLayout()
        self.layout.addWidget(self.color_picker, 0, 0)
        self.layout.addWidget(self.size_picker, 1, 0)
        self.layout.addLayout(self.brush_type_picker, 0, 1, 2, 1)
        self.setLayout(self.layout)
        self.setFixedHeight(150)
