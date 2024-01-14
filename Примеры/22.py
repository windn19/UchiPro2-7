import sys

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        button = QPushButton('Кнопка', self)
        button2 = QPushButton('Кнопка2', self)
        button.clicked.connect(lambda args: self.func(1, 2, 3, 4, 5))
        button2.clicked.connect(lambda args: self.func('hello'))
        layout.addWidget(button)
        layout.addWidget(button2)
        self.setLayout(layout)

    def func(self, *args):
        print(args)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
