from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,QGroupBox, QRadioButton, QButtonGroup

app = QApplication([])
main_win = QWidget()

btn_ok = QPushButton('Ответить')
lb_q = QLabel('Вопрос')

rgb = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(rbtn_1)
layout2.addWidget(rbtn_2)
layout3.addWidget(rbtn_3)
layout3.addWidget(rbtn_4)

layout1.addLayout(layout2)
layout1.addLayout(layout3)

rgb.setLayout(layout1)

AnsGroupBox = QGroupBox('Результат')
lb_res = QLabel('прав или нет')
lb_cor = QLabel('Ответ тут')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_res, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_cor, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layoutline1 = QHBoxLayout()
layoutline2 = QHBoxLayout()
layoutline3 = QHBoxLayout()

layoutline1.addWidget(lb_q, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layoutline2.addWidget(rgb)
layoutline2.addWidget(AnsGroupBox)
rgb.hide()

layoutline3.addStretch(1)
layoutline3.addWidget(btn_ok, stretch=2)
layoutline3.addStretch(1)

layoutcard = QVBoxLayout()

layoutcard.addLayout(layoutline1, stretch=2)
layoutcard.addLayout(layoutline2, stretch=8)
layoutcard.addStretch(2)
layoutcard.addLayout(layoutline3, stretch=1)
layoutcard.addStretch(1)

def show_res():
    rgb.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')

def show_ques():
    rgb.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
'''
def test():
    if 'Ответить' == btn_ok.text():
        show_res()
    else:
        show_ques()
'''
btn_ok.clicked.connect(test)
main_win.setLayout(layoutcard)
main_win.show()
app.exec_()