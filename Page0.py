from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QWidget


class Page0(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.vlayout = QVBoxLayout()
        self.text = QLineEdit()
        self.button = QPushButton('提交')
        self.text.setFixedSize(240, 30)
        self.button.setFixedSize(80, 30)
        self.button.clicked.connect(self.__submit_text)
        self.vlayout.addWidget(self.text)
        self.vlayout.addWidget(self.button)
        self.vlayout.setContentsMargins(10, 10, 10, 10)
        self.vlayout.setSpacing(30)
        self.vlayout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.vlayout)

    def __submit_text(self):
        text = self.text.text()
        if text.strip() != "":
            QMessageBox.information(self, '提示', text)
