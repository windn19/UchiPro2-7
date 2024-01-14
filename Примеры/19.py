import sys

from PyQt6.QtWidgets import (QWidget, QApplication, QLineEdit,
                             QLabel, QVBoxLayout)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        lineEdit = QLineEdit(self)
        label = QLabel(self)
        lineEdit.textChanged.connect(label.setText)
        layout.addWidget(lineEdit)
        layout.addWidget(label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
