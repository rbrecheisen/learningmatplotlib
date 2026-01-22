import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())