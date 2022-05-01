from tkinter import CENTER
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,
QPushButton,QVBoxLayout,QHBoxLayout, QLineEdit, QLabel, QMessageBox, QRadioButton)
from intr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle('ВТОРОЕ ОКНО')
        self.resize(win_width, win_height)
        self.move(win_x,win_y)

    def initUI(self):
        self.label_name=QLabel("Введите ФИО")
        self.line_lf_name=QLineEdit('Ф.И.О')

        self.label_age=QLabel('Полных лет')
        self.line_age=QLineEdit('0')

        self.label_inst_1=QLabel(intstr_1)
        self.btn_test_1=QPushButton('Начать первый тест')

        self.line_bpm_1=QLineEdit('Введите количество ударов в минуту')

        self.check_res=QPushButton('Узнать результат')

        self.layout_vert_left=QVBoxLayout()
        self.layout_vert_right=QVBoxLayout()
        self.total_layout=QHBoxLayout()
        self.layout_vert_left.addWidget(self.label_name)
        self.layout_vert_left.addWidget(self.line_lf_name)
        self.layout_vert_left.addWidget(self.label_age)
        self.layout_vert_left.addWidget(self.line_age) 
        self.layout_vert_left.addWidget(self.label_inst_1)
        self.layout_vert_left.addWidget(self.line_bpm_1)
        self.layout_vert_left.addWidget(self.check_res,alignment=Qt.AlignRight)

   
        self.setLayout(self.layout_vert_left)

    def connects(self):
        pass

    def next_click(self):
        pass
        
