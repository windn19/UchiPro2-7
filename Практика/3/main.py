import sys

from PyQt6.QtWidgets import QWidget, QApplication
from design import Ui_Form


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.coords = [
            [self.pushButton00, self.pushButton01, self.pushButton02],
            [self.pushButton10, self.pushButton11, self.pushButton12],
            [self.pushButton20, self.pushButton21, self.pushButton22],
        ]
        for row in range(3):
            for col in range(3):
                self.coords[row][col].clicked.connect(self.click)
        self.pushButtonRepeat.clicked.connect(self.restart)
        self.char = 'X'

    def setButtons(self, value):
        for row in range(3):
            for col in range(3):
                self.coords[row][col].setEnabled(value)

    def click(self):
        print(self.sender())
        for row in range(3):
            for col in range(3):
                if self.coords[row][col] == self.sender():
                    self.coords[row][col].setEnabled(False)
                    self.coords[row][col].setText(self.char)
                    if self.char == 'X':
                        self.char = 'O'
                    else:
                        self.char = 'X'

    def restart(self):
        for row in range(3):
            for col in range(3):
                self.coords[row][col].setText('')
        self.setButtons(True)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    auth = Window()
    auth.show()
    sys.exit(app.exec())
