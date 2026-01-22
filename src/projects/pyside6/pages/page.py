from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QLineEdit,
)
from mplcanvas import MplCanvas


class Page(QWidget):
    def __init__(self, parent=None):
        super(Page, self).__init__(parent)
        self._canvas = None
        self._form_layout = None
        self._fields = []
        self.add_line_edit(title='Hello')
        self.init()

    def init(self):
        for field in self._fields:
            self.form_layout().addRow(field['title'], field['widget'])
        layout = QVBoxLayout()
        layout.addLayout(self.form_layout())
        layout.addWidget(self.canvas().navigation_toolbar())
        layout.addWidget(self.canvas())
        self.setLayout(layout)

    def canvas(self):
        if not self._canvas:
            self._canvas = MplCanvas(self, width=6, height=4)
        return self._canvas
    
    def form_layout(self):
        if not self._form_layout:
            self._form_layout = QFormLayout()
        return self._form_layout
    
    # FIELDS

    def add_line_edit(self, title, placeholder=''):
        self._fields.append({'title': title, 'widget': QLineEdit(placeholderText=placeholder)})