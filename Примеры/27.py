import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel(self)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        print(f'Вы нажали кнопку: {event.button()}')
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText('Вы нажали левую кнопку мыши')
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText('Вы нажали правую кнопку мыши')
        print(event.pos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
