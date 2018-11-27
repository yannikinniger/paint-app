from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QMenu, QFileDialog

from src.MenuItem import setup_menu_item


class FileMenu(QMenu):

    file_options = "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)"  # available file options

    def __init__(self, main_menu, canvas, window):
        super().__init__(' File', parent=main_menu)
        self.canvas = canvas
        self.window = window
        self.__setup_actions()

    def __setup_actions(self):
        save_action = setup_menu_item(' Save', '../icons/save.png', 'Ctrl+S', self.save, self.window)
        self.addAction(save_action)
        open_action = setup_menu_item(' Open', '../icons/open.png', 'Ctrl+O', self.open, self.window)
        self.addAction(open_action)
        clear_action = setup_menu_item(' Clear', '../icons/clear.png', 'Ctrl+Alt+C', self.clear, self.window)
        self.addAction(clear_action)
        exit_action = setup_menu_item(' Exit', '../icons/exit.png', 'Ctrl+E', FileMenu._exit, self.window)
        self.addAction(exit_action)

    def save(self):
        """
        Saves the drawings on the canvas to a picture file
        """
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", FileMenu.file_options)
        if file_path == "":
            return
        self.canvas.image.save(file_path)

    def open(self):
        """
        Opens an existing picture and loads it to the canvas
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", FileMenu.file_options)
        loaded_image = QImage()
        loaded_image.load(file_path)
        self.canvas.image = loaded_image
        self.canvas.update()

    def clear(self):
        """
        Clears the canvas
        """
        self.canvas.image.fill(Qt.white)
        self.canvas.update()

    @staticmethod
    def _exit():
        """
        Exits the application with a 0 code
        """
        exit(0)
