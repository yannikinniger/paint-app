from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


def setup_menu_item(name, icon_path, shortcut, action, window):
    """
    Sets up a QAction, which can be used as a menu item
    :param name: Name of the action
    :param icon_path: Path of the icon to be used
    :param shortcut: Shortcut of the action
    :param action: Function which should be executed on the action
    :param window: Window the action belongs to
    :return: Assembled QAction
    """
    menu_item = QAction(QIcon(icon_path), name, window)
    menu_item.setShortcut(shortcut)
    menu_item.triggered.connect(action)
    return menu_item
