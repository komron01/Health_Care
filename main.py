from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,
    QPushButton,QVBoxLayout,QHBoxLayout,QLabel, QMessageBox, QRadioButton)


app = QApplication([]) #создать само приложение
main_win=QWidget()    # создать главное окно
main_win.setWindowTitle('Вопросы')

question=QLabel('В каком году родился Никита?')
btn_answer1=QRadioButton('2000')
btn_answer2=QRadioButton('2022')
btn_answer3=QRadioButton('2005')
btn_answer4=QRadioButton('2010')

layoutH1=QHBoxLayout()
layoutH2=QHBoxLayout()
layoutH3=QHBoxLayout()

layoutH1.addWidget(question,alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer1,alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment=Qt.AlignCenter)

layout_main=QVBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)

main_win.setLayout(layout_main)
print('Hello world')

main_win.show()         # вывести главное окно
app.exec_()             # оставить окно пока нет взаимодействии 
