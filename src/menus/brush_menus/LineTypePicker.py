from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QRadioButton, QHBoxLayout, QSizePolicy


class LineTypePicker(QGroupBox):

    def __init__(self, brush):
        super().__init__('Line Type')
        self.brush = brush

        self.solid_line = QRadioButton('Solid')
        self.solid_line.setChecked(True)
        self.dashed_line = QRadioButton('Dashed')
        self.dot_line = QRadioButton('Doted')

        self.__layout()
        self.__controls()

    def __layout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.solid_line)
        layout.addWidget(self.dashed_line)
        layout.addWidget(self.dot_line)
        self.setLayout(layout)

    def __controls(self):
        self.solid_line.toggled.connect(lambda: self.change_line_type(Qt.SolidLine))
        self.dashed_line.toggled.connect(lambda: self.change_line_type(Qt.DashLine))
        self.dot_line.toggled.connect(lambda: self.change_line_type(Qt.DotLine))

    def change_line_type(self, line_type):
        """
        Sets the a new line type on the brush
        :param line_type: Line type from QtCore.Qt
        """
        self.brush.line_type = line_type
