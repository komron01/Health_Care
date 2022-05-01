from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,
    QPushButton,QVBoxLayout,QHBoxLayout,QLabel, QMessageBox, QRadioButton)
from intr import *
from second_app import TestWin

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x,win_y)

    def initUI(self):
        self.hello=QLabel(txt_hello)
        self.description=QLabel(txt_desc)
        self.button=QPushButton(txt_button)
        self.layout=QVBoxLayout()
        self.layout.addWidget(self.hello)
        self.layout.addWidget(self.description)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw=TestWin()


app=QApplication([])
main_menu=MainWin()
app.exec()
