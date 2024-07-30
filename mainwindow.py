from PySide2.QtWidgets import QHBoxLayout, QMainWindow, QTabWidget, QWidget
from PySide2.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1024, 768)
        self.setWindowTitle('PySide2Demo')
        self.setCentralWidget(QWidget())

        self.__init_widget()

    def __init_widget(self):
        self.tab = QTabWidget()
        self.hl = QHBoxLayout()
        self.hl.setContentsMargins(10, 10, 10, 10)
        self.hl.setAlignment(Qt.AlignCenter)
        self.hl.addWidget(self.tab)
        self.centralWidget().setLayout(self.hl)