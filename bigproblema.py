import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(650, 300, 600, 600)

        self.adress_label = QLabel(self)
        self.adress_label.setText("Введите адрес: ")
        self.adress_label.move(40, 90)

        self.adress_input = QLineEdit(self)
        self.adress_input.move(160, 90)

        self.mash_label = QLabel(self)
        self.mash_label.setText("Введите масштаб: ")
        self.mash_label.move(40, 135)

        self.mash_input = QLineEdit(self)
        self.mash_input.move(160, 135)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())