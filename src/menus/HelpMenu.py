from PyQt5.QtWidgets import QMenu, QMessageBox

from src.MenuItem import setup_menu_item


class HelpMenu(QMenu):

    def __init__(self, main_menu, window):
        super().__init__(' Help', parent=main_menu)
        self.window = window
        self.__setup_actions()

    def __setup_actions(self):
        about_action = setup_menu_item(' About Program', '../icons/info.png', 'Ctrl+Alt+A', self.show_about, self.window)
        self.addAction(about_action)

    @staticmethod
    def show_about():
        """
        Displays an about popup on the screen
        """
        about = QMessageBox()
        about.setText("About")
        about.setInformativeText("Made by: Yannik Inniger")
        about.setWindowTitle("About")
        about.setDetailedText("This is a simple drawing Application made with PyQt.")
        about.setStandardButtons(QMessageBox.Ok)
        about.exec()

