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
