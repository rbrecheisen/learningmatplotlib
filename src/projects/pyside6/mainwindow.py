from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
)
from pages.page import Page


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._stacked_widget = None
        self.init()

    def init(self):
        self.setCentralWidget(self.stacked_widget())
        self.setWindowTitle('Matplotlib')

    def stacked_widget(self):
        if not self._stacked_widget:
            self._stacked_widget = QStackedWidget()
            self._stacked_widget.addWidget(Page(self))
        return self._stacked_widget
