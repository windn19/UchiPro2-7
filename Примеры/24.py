import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel(self)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def keyPressEvent(self, event):
        self.label.setText(f'Вы нажали клавишу: {event.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
