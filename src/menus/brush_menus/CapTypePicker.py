from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QGroupBox, QRadioButton, QVBoxLayout
from qtpy import QtCore


class CapTypePicker(QGroupBox):
    """
    Provides a picker for the various cap types of the brush
    """

    def __init__(self, brush):
        super().__init__('Cap Type')
        self.brush = brush

        self.round_cap = CapTypePicker.init_radio_button('Round', lambda: self.change_cap_type(Qt.RoundCap))
        self.round_cap.setChecked(True)
        self.square_cap = CapTypePicker.init_radio_button('Square', lambda: self.change_cap_type(Qt.SquareCap))
        self.flat_cap = CapTypePicker.init_radio_button('Flat', lambda: self.change_cap_type(Qt.FlatCap))

        self.__layout()

    def __layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.round_cap)
        layout.addWidget(self.square_cap)
        layout.addWidget(self.flat_cap)
        layout.setSpacing(15)
        self.setLayout(layout)

    def change_cap_type(self, new_cap_type):
        """
        Changes the cap type of the brush
        :param new_cap_type: Cap type to set from QtCore.Qt
        """
        self.brush.cap_type = new_cap_type

    @staticmethod
    def init_radio_button(name, on_trigger_function):
        """
        Helper method to simplify the creation of Radio buttons
        :param name: Label for the Button, the name of the icon should be the same
        :param on_trigger_function: Function which should be triggered if the button is selected
        :return: Assembled radio button
        """
        radio_button = QRadioButton(name)
        icon = QIcon('../icons/caps/{}.png'.format(name))
        radio_button.setIcon(icon)
        radio_button.setIconSize(QtCore.QSize(15, 15))
        radio_button.toggled.connect(on_trigger_function)
        return radio_button
