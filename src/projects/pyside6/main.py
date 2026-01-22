import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):
    def __init__(self, parent, width, height, nrows=1, ncols=1, dpi=100):
        self._figure = Figure(figsize=(width, height), dpi=dpi)
        self._axes = self._figure.subplots(nrows, ncols)
        self._figure.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
        super(MplCanvas, self).__init__(self._figure)
        self.setParent(parent)
        self._navigation_toolbar = NavigationToolbar(self, parent)

    def figure(self):
        return self._figure
    
    def axes(self, index=0):
        if isinstance(self._axes, list):
            return self._axes[index]
        return self._axes
    
    def navigation_toolbar(self):
        return self._navigation_toolbar


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._canvas = None
        self.init()

    def init(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.canvas().navigation_toolbar())
        layout.addWidget(self.canvas())
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setWindowTitle('Matplotlib with PySide6')
        self.canvas().axes().plot([0, 1, 2], [0, 1, 0])
        self.canvas().axes().set_axis_off()
        self.canvas().draw()

    def canvas(self):
        if not self._canvas:
            self._canvas = MplCanvas(self, width=6, height=4)
        return self._canvas


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())