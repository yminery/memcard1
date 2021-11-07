from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, 
QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, 
QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
correct= 0
ans_count = 0

app = QApplication([])
window = QWidget()

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Сколько будет 1000-7')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('69')
rbtn_2 = QRadioButton('993')
rbtn_3 = QRadioButton('6')
rbtn_4 = QRadioButton('1003')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignVCenter | Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 3)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def next_question():
    global correct, ans_count
    last_q = question_list[window.question]
    window.question += 1
    if window.question >= len(question_list):
        window.question = 0
        print('Результат:\nВсего вопросов:{0}\nПравильных ответов:{1}\nРейтинг:{2}%'.format(ans_count, correct, correct/ans_count*100))
        shuffle(question_list)    
    q = question_list[window.question]
    while q == last_q:
        shuffle(question_list)
        q = question_list[window.question]
    ask(q)
def show_correct(res):
    lb_Result.setText(res)
    show_result()

def test():
    global correct, ans_count
    if answers[0].isChecked():
        show_correct('Верно!')
        ans_count +=1 
        correct += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно!')
        ans_count -=1
        correct -=1

def click_OK():
    if btn_OK.text() == 'Ответить':
        test()
    else:
        next_question()

q = Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')
question_list = []
question_list.append(q)
question_list.append(Question('1000-7', '993', '998', '4', '21'))
question_list.append(Question('8-7', '5', '1', '4', '21'))
question_list.append(Question('145-7', '138', '998', '4', '2442'))
question_list.append(Question('923-923', '993', '0', '6', '11'))
window.question = -1
shuffle(question_list)
next_question()
btn_OK.clicked.connect(click_OK)
window.setLayout(layout_card)
window.show()
app.exec_()