import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication

from design import Ui_Form


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.expression = ''
        self.toolButton_0.clicked.connect(self.buttonPressed)
        self.toolButton_1.clicked.connect(self.buttonPressed)
        self.toolButton_2.clicked.connect(self.buttonPressed)
        self.toolButton_3.clicked.connect(self.buttonPressed)
        self.toolButton_4.clicked.connect(self.buttonPressed)
        self.toolButton_5.clicked.connect(self.buttonPressed)
        self.toolButton_6.clicked.connect(self.buttonPressed)
        self.toolButton_7.clicked.connect(self.buttonPressed)
        self.toolButton_8.clicked.connect(self.buttonPressed)
        self.toolButton_9.clicked.connect(self.buttonPressed)
        self.toolButton_plus.clicked.connect(self.buttonPressed)
        self.toolButton_min.clicked.connect(self.buttonPressed)
        self.toolButton_mul.clicked.connect(self.buttonPressed)
        self.toolButton_div.clicked.connect(self.buttonPressed)
        self.toolButton_point.clicked.connect(self.buttonPressed)
        self.toolButton_reset.clicked.connect(self.buttonPressed)
        self.toolButton_power.clicked.connect(self.buttonPressed)
        self.toolButton.clicked.connect(self.buttonPressed)

    def buttonPressed(self):
        sender = self.sender().text()
        if sender == 'C':
            self.expression = ''
            self.lcdNumber.display(0)
        elif sender == '=':
            try:
                result = eval(self.expression)
                self.lcdNumber.display(str(round(result, 2)))
            except:
                self.lcdNumber.display('error')
            self.expression = ''
        else:
            self.expression += sender
        self.lineEdit.setText(self.expression)

    def keyPressEvent(self, event):
        key = event.text()
        if key.isdigit() or key in ['+', '-', '*', '/', '**', '.']:
            self.expression += key
        if event.key() == Qt.Key.Key_Escape:
            self.expression = ''
            self.lcdNumber.display(0)
        elif event.key() == Qt.Key.Key_Enter:
            try:
                result = eval(self.expression)
                self.lcdNumber.display(str(round(result, 2)))
            except:
                self.lcdNumber.display('error')
            self.expression = ''
        self.lineEdit.setText(self.expression)



if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    auth = Window()
    auth.show()
    sys.exit(app.exec())
