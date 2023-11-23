import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow
from ui.ui import MainView, SettingsView, LogView


class MainWindow(QMainWindow):
    def __init__(self, button_callbacks):
        super().__init__()

        self.button_callbacks = button_callbacks

        # Set the custom widget as the central widget
        self.change_view("main")

        # Set window properties
        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle("Dlux")
        self.setFixedSize(1000, 800)

    def change_view(self, key):
        if key == "settings":
            settings_view = SettingsView(self.button_callbacks)
            self.setCentralWidget(settings_view)
        elif key == "main":
            main_view = MainView(self.button_callbacks)
            self.setCentralWidget(main_view)
        elif key == "log":
            log_view = LogView(self.button_callbacks)
            self.setCentralWidget(log_view)


class Controller:
    def __init__(self) -> None:
        # button callback mappings
        self.button_callbacks = {
            "settings": self.onClickSettings,
            "log": self.onClickLog,
            "back": self.onClickBack,
        }

        self.setup_ui()

    def onClickSettings(self):
        print("settings!")
        self.window.change_view("settings")

    def onClickLog(self):
        print("log!")
        self.window.change_view("log")

    def onClickBack(self):
        print("back!")
        self.window.change_view("main")

    def setup_ui(self):
        self.app = QApplication([])
        self.window = MainWindow(self.button_callbacks)

    def start_ui(self):
        # Show the window
        self.window.show()

        sys.exit(self.app.exec())


c = Controller()
c.start_ui()
