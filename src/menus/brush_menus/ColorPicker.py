import re

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton, QColorDialog, QGroupBox, QHBoxLayout, QLineEdit

from src.brush.BrushObserver import BrushObserver


class ColorPicker(BrushObserver, QGroupBox):
    """
    Provides ways to change the color of the brush
    """

    def __init__(self, brush):
        QGroupBox.__init__(self, 'Color')
        BrushObserver.__init__(self, brush)

        self.color_display = QPushButton()
        self.hex_color = QLineEdit()
        self.__init_components()
        self.__layout()
        self.__controls()

        self.update_brush()

    def __init_components(self):
        self.color_display.setFixedHeight(30)
        self.hex_color.setText(self.brush.brush_color.name())
        self.hex_color.setFixedWidth(65)

    def __layout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.color_display)
        layout.addWidget(self.hex_color)
        self.setLayout(layout)
        self.setAlignment(Qt.LeftSection)

    def __controls(self):
        self.color_display.clicked.connect(self.set_color_from_color_picker)
        self.hex_color.textChanged.connect(self.set_hex_color)

    def set_color_from_color_picker(self):
        """
        Opens a color dialog and sets the value on the brush
        """
        new_color = QColorDialog.getColor(initial=self.brush.brush_color)
        if new_color.isValid():
            self.brush.brush_color = new_color

    def set_hex_color(self):
        """
        Gets the hex color from the text field and sets it as the new brush
        color if a valid hex color was entered
        """
        hex_color = self.hex_color.text()
        if ColorPicker.is_hex_color(hex_color):
            self.hex_color.setStyleSheet('color: black')
            red, green, blue = ColorPicker.hex_to_rgb(hex_color)
            self.brush.brush_color = QColor(red, green, blue)
        else:
            self.hex_color.setStyleSheet('color: red')

    def update_brush(self):
        color_code = self.brush.brush_color.name()
        self.color_display.setStyleSheet('background-color: {}'.format(color_code))
        self.hex_color.setText(color_code)

    @staticmethod
    def is_hex_color(hex_code):
        """
        Checks if the color is a valid hex color code
        Regex from: http://www.mkyong.com/regular-expressions/how-to-validate-hex-color-code-with-regular-expression
        :param hex_code: Hex color code including #
        :return: Boolean if the given color code is valid
        """
        return re.match('^#([A-Fa-f0-9]{6})$', hex_code)

    @staticmethod
    def hex_to_rgb(hex_code):
        """
        Converts a hex color valid code to it's RGB values
        :param hex_code: Valid hex color code
        :return: Tuple of the RGB values
        """
        hex_code = hex_code.strip('#')
        return tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4))
