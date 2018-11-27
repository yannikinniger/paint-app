from PyQt5.QtWidgets import QPushButton, QGridLayout

from src.menus.brush_menus.CapTypePicker import CapTypePicker
from src.menus.brush_menus.JoinTypePicker import JoinTypePicker
from src.menus.brush_menus.LineTypePicker import LineTypePicker


class BrushTypePicker(QGridLayout):
    """
    Combines the more specific attributes of the brush in one layout
    and gives the option to hide more advanced tools
    """

    def __init__(self, brush):
        super().__init__()

        self.show_advanced = False
        self.line_type = LineTypePicker(brush)
        self.join_type = JoinTypePicker(brush)
        self.join_type.setVisible(self.show_advanced)
        self.cap_type = CapTypePicker(brush)
        self.cap_type.setVisible(self.show_advanced)
        self.advanced_toggle = QPushButton('Show Advanced Options')
        self.__layout()
        self.__controls()

    def __layout(self):
        self.addWidget(self.line_type, 0, 0)
        self.addWidget(self.advanced_toggle, 1, 0)
        self.addWidget(self.join_type, 0, 1, 2, 1)
        self.addWidget(self.cap_type, 0, 2, 2, 1)

    def __controls(self):
        self.advanced_toggle.clicked.connect(self.toggle_advanced_options)

    def toggle_advanced_options(self):
        """
        Toggles the advanced settings of the brush
        """
        self.show_advanced = not self.show_advanced
        self.join_type.setVisible(self.show_advanced)
        self.cap_type.setVisible(self.show_advanced)
        if self.show_advanced:
            self.advanced_toggle.setText('Hide Advanced Options')
        else:
            self.advanced_toggle.setText('Show Advanced Options')
