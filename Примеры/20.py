import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        button_1 = QPushButton("Нажми меня 1", self)
        button_2 = QPushButton("Нажми меня 2", self)
        button_1.clicked.connect(self.func)
        button_2.clicked.connect(self.func)
        layout.addWidget(button_1)
        layout.addWidget(button_2)
        self.setLayout(layout)

    def func(self):
        sender = self.sender()
        print(sender)
        print(sender.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
