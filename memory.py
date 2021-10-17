from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,QGroupBox, QRadioButton

app = QApplication([])
main_win = QWidget()

btn_ok = QPushButton('goooo')
lb_q = QLabel('1000-7')

rgb = QGroupBox('DDDDD')
rbtn_1 = QRadioButton('6')
rbtn_2 = QRadioButton('993')
rbtn_3 = QRadioButton('хз')
rbtn_4 = QRadioButton('-1')

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

layoutline1 = QHBoxLayout()
layoutline2 = QHBoxLayout()
layoutline3 = QHBoxLayout()

layoutline1.addWidget(lb_q, alignment=(Qt.AlignVCenter | Qt.AlignHCenter))
layoutline2.addWidget(rgb)
layoutline3.addStretch(1)
layoutline3.addWidget(btn_ok, stretch=3)
layoutline3.addStretch(1)

layoutcard = QVBoxLayout()

layoutcard.addLayout(layoutline1, stretch=2)
layoutcard.addLayout(layoutline2, stretch=8)
layoutcard.addStretch(2)
layoutcard.addLayout(layoutline3, stretch=1)
layoutcard.addStretch(1)

main_win.setLayout(layoutcard)

main_win.show()
app.exec_()