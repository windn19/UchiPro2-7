import sys

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        button = QPushButton('Кнопка', self)
        button.clicked.connect(self.func)
        layout.addWidget(button)
        self.setLayout(layout)

    def func(self):
        print('Тест')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
