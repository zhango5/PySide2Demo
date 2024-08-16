from PySide2.QtCore import Qt
from PySide2.QtWidgets import QHBoxLayout, QMainWindow, QTabWidget, QWidget

from Page0 import Page0
from Page1 import Page1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1024, 768)
        self.setWindowTitle('PySide2Demo')
        self.setCentralWidget(QWidget())

        self.__init_widget()
        self.__init_page0()
        self.__init_page1()

    def __init_widget(self):
        self.tab = QTabWidget()
        self.hl = QHBoxLayout()
        self.hl.setContentsMargins(10, 10, 10, 10)
        self.hl.setAlignment(Qt.AlignCenter)
        self.hl.addWidget(self.tab)
        self.centralWidget().setLayout(self.hl)

    def __init_page0(self):
        self.tab.addTab(Page0(), "Page 0")

    def __init_page1(self):
        self.tab.addTab(Page1(), "Page 1")
