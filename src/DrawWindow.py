from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QToolBar

from src.Canvas import Canvas
from src.brush.Brush import Brush
from src.menus.DrawMenu import DrawMenu
from src.menus.FileMenu import FileMenu
from src.menus.HelpMenu import HelpMenu


class DrawWindow(QMainWindow):

    def __init__(self, screen_resolution):
        super().__init__()
        self.setWindowTitle('Paint Application')
        start_x, start_y = self.calculate_start_position(screen_resolution)
        self.setGeometry(start_x, start_y, 800, 600)
        self.setWindowIcon(QIcon("../icons/paint-brush_menus.png"))

        self.brush = Brush()
        self.canvas = Canvas(self, self.brush)
        self.toolbar = self.init_toolbar(self.brush)

        self.__setup_menus()
        self.__layout()

    def __layout(self):
        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.canvas)

    def __setup_menus(self):
        main_menu = self.menuBar()

        file_menu = FileMenu(main_menu, self.canvas, self)
        main_menu.addMenu(file_menu)
        help_menu = HelpMenu(main_menu, self)
        main_menu.addMenu(help_menu)

    def init_toolbar(self, brush):
        """
        Initializes a draw menu and makes a toolbar out of it
        :param brush: Brush which can be observed by all BrushObservables
        :return: Assembled QToolBar
        """
        toolbar = QToolBar()
        draw_menu = DrawMenu(self, brush)
        toolbar.addWidget(draw_menu)
        toolbar.setMinimumHeight(100)
        return toolbar

    @staticmethod
    def calculate_start_position(screen_resolution):
        """
        Calculates the coordinates to place the window in the middle of the screen
        :param screen_resolution: Resolution of the screen the window was opened
        :return: x and y coordinates of the window to be centered
        """
        x = (screen_resolution.width() / 2) - 400
        y = (screen_resolution.height() / 2) - 350
        return x, y
