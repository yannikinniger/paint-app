from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QSlider


class SizePicker(QGroupBox):

    def __init__(self, brush):
        super().__init__('Brush Size')
        self.brush = brush

        self.size_slider = QSlider(Qt.Horizontal)

        self.__init_parts()
        self.__layout()
        self.__controls()

    def __init_parts(self):
        self.size_slider.setRange(1, 30)
        self.size_slider.setValue(self.brush.brush_size)
        self.size_slider.setMinimumWidth(200)
        self.setMaximumWidth(300)

    def __layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.size_slider)
        self.setLayout(layout)

    def __controls(self):
        self.size_slider.valueChanged.connect(self.change_brush_size)

    def change_brush_size(self):
        """
        Gets the value of the slider and sets it as a new brush size
        """
        self.brush.brush_size = self.size_slider.value()
