from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QGroupBox, QHBoxLayout


class JoinTypePicker(QGroupBox):

    def __init__(self, brush):
        super().__init__('Join Type')
        self.brush = brush

        self.picker = QComboBox()
        self.picker.addItem('Bevel')
        self.picker.addItem('Miter')
        self.picker.addItem('Round')

        self.__layout()
        self.picker.currentIndexChanged.connect(self.join_type_changed)

    def __layout(self):
        layout = QHBoxLayout()
        layout.addWidget(self.picker)
        self.setLayout(layout)

    def join_type_changed(self):
        """
        Converts the String value from the picker to a valid join type
        and sets it on the brush
        """
        new_type = self.picker.currentText()
        if new_type == 'Bevel':
            self.brush.join_type = Qt.BevelJoin
        elif new_type == 'Miter':
            self.brush.join_type = Qt.MiterJoin
        elif new_type == 'Round':
            self.brush.join_type = Qt.RoundJoin
        else:
            raise ValueError('Invalid join brush_menus type selected')
