import sys

from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QWidget, QApplication

from design import Ui_Form


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.textEdited.connect(self.fromDec)
        self.lineEdit_2.textEdited.connect(self.fromBin)
        self.lineEdit_3.textEdited.connect(self.fromOct)
        self.lineEdit_4.textEdited.connect(self.fromHex)

    def fromDec(self):
        if self.lineEdit.text():
            try:
                dec = int(self.lineEdit.text())
                self.lineEdit_2.setText(f'{dec:b}')
                self.lineEdit_3.setText(f'{dec:o}')
                self.lineEdit_4.setText(f'{dec:x}'.upper())
            except ValueError:
                self.lineEdit_2.setText('Ошибка')
                self.lineEdit_3.setText('Ошибка')
                self.lineEdit_4.setText('Ошибка')

    def fromBin(self):
        if self.lineEdit_2.text():
            try:
                dec = int(self.lineEdit_2.text(), 2)
                self.lineEdit.setText(f'{dec}')
                self.lineEdit_3.setText(f'{dec:o}')
                self.lineEdit_4.setText(f'{dec:x}'.upper())
            except ValueError:
                self.lineEdit.setText('Ошибка')
                self.lineEdit_3.setText('Ошибка')
                self.lineEdit_4.setText('Ошибка')

    def fromOct(self):
        if self.lineEdit_3.text():
            try:
                dec = int(self.lineEdit_3.text(), 8)
                self.lineEdit.setText(f'{dec}')
                self.lineEdit_2.setText(f'{dec:b}')
                self.lineEdit_4.setText(f'{dec:x}'.upper())
            except ValueError:
                self.lineEdit.setText('Ошибка')
                self.lineEdit_2.setText('Ошибка')
                self.lineEdit_4.setText('Ошибка')

    def fromHex(self):
        if self.lineEdit_4.text():
            try:
                dec = int(self.lineEdit_4.text(), 16)
                self.lineEdit.setText(f'{dec}')
                self.lineEdit_2.setText(f'{dec:b}')
                self.lineEdit_3.setText(f'{dec:o}')
            except ValueError:
                self.lineEdit.setText('Ошибка')
                self.lineEdit_2.setText('Ошибка')
                self.lineEdit_3.setText('Ошибка')


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    auth = Window()
    auth.show()
    sys.exit(app.exec())
