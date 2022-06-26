import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Калькулятор')
        self.setGeometry(150, 150, 400, 500)

        self.background_color = (66, 64, 87)

        self.setStyleSheet('background: rgb{}; border-radius: 10px;'.format(self.background_color))

        layout = QGridLayout()

        #цифры
        self.text = QtWidgets.QLabel(self)
        self.text.setText('0')
        self.text.setFont(QFont('Arial', 16))
        self.text.setStyleSheet('color: rgb(158, 150, 250); margin-top: 50px; margin-bottom: 50px;')

        self.color = (59, 54, 115)
        self.text_color = (158, 150, 250)

        self.colvo_start = 0
        self.colvo_end = 0

        self.color_button = (173, 158, 80)
        self.color_button_2 = (222, 91, 91)
        self.color_button_3 = (91, 104, 222)
        self.border_color = (37, 41, 77)
        self.border_color_2 = (82, 74, 35)
        self.border_color_3 = (57, 65, 133)
        self.text_color_2 = (250, 231, 137)
        self.text_color_3 = (139, 175, 247)

        layout.addWidget(self.text, 0, 0, 1, 4, alignment=Qt.AlignRight)

        btn7 = QPushButton('7')
        btn7.setStyleSheet('background: rgb{}; color: rgb{}; border: 2px dashed rgb{};'.format(self.color, self.text_color, self.border_color))
        btn7.clicked.connect(self.set_symbol(btn7.text()))
        btn7.setFont(QFont('Arial', 13))

        btn8 = QPushButton('8')
        btn8.setStyleSheet('background: rgb{}; color: rgb{}; border: 2px dashed rgb{};'.format(self.color, self.text_color, self.border_color))
        btn8.clicked.connect(self.set_symbol(btn8.text()))
        btn8.setFont(QFont('Arial', 13))

        btn9 = QPushButton('9')
        btn9.setStyleSheet('background: rgb{}; color: rgb{}; border: 2px dashed rgb{};'.format(self.color, self.text_color, self.border_color))
        btn9.clicked.connect(self.set_symbol(btn9.text()))
        btn9.setFont(QFont('Arial', 13))

        btn4 = QPushButton('4')
        btn4.clicked.connect(self.set_symbol(btn4.text()))
        btn4.setStyleSheet('background: rgb{}; color: rgb{}; border: 2px dashed rgb{};'.format(self.color, self.text_color, self.border_color))
        btn4.setFont(QFont('Arial', 13))

        btn5 = QPushButton('5')
        btn5.clicked.connect(self.set_symbol(btn5.text()))
        btn5.setStyleSheet('background: rgb{}; color: rgb{}; border: 2px dashed rgb{};'.format(self.color, self.text_color, self.border_color))
        btn5.setFont(QFont('Arial', 13))

        btn6 = QPushButton('6')
        btn6.clicked.connect(self.set_symbol(btn6.text()))
        btn6.setStyleSheet('background: rgb{}; color: rgb{}; border: 2px dashed rgb{};'.format(self.color, self.text_color, self.border_color))
        btn6.setFont(QFont('Arial', 13))

        btn1 = QPushButton('1')
        btn1.clicked.connect(self.set_symbol(btn1.text()))
        btn1.setStyleSheet('background: rgb{}; color: rgb{}; border: 2px dashed rgb{};'.format(self.color, self.text_color, self.border_color))
        btn1.setFont(QFont('Arial', 13))

        btn2 = QPushButton('2')
        btn2.clicked.connect(self.set_symbol(btn2.text()))
        btn2.setStyleSheet('background: rgb{}; color: rgb{}; border: 2px dashed rgb{};'.format(self.color, self.text_color, self.border_color))
        btn2.setFont(QFont('Arial', 13))

        btn3 = QPushButton('3')
        btn3.clicked.connect(self.set_symbol(btn3.text()))
        btn3.setStyleSheet('background: rgb{}; color: rgb{}; border: 2px dashed rgb{};'.format(self.color, self.text_color, self.border_color))
        btn3.setFont(QFont('Arial', 13))

        btn0 = QPushButton('0')
        btn0.clicked.connect(self.set_symbol(btn0.text()))
        btn0.setStyleSheet('background: rgb{}; color: rgb{}; border: 2px dashed rgb{};'.format(self.color, self.text_color, self.border_color))
        btn0.setFont(QFont('Arial', 13))

        layout.addWidget(btn7, 2, 0)
        layout.addWidget(btn8, 2, 1)
        layout.addWidget(btn9, 2, 2)

        layout.addWidget(btn4, 3, 0)
        layout.addWidget(btn5, 3, 1)
        layout.addWidget(btn6, 3, 2)

        layout.addWidget(btn1, 4, 0)
        layout.addWidget(btn2, 4, 1)
        layout.addWidget(btn3, 4, 2)

        layout.addWidget(btn0, 5, 2)

        #операции
        self.operations = ['+', '-', '*', '/', '%']
        self.not_number_operations = ['+', '*', '/', '%']

        btnplus = QPushButton('+')
        btnplus.clicked.connect(self.set_operation(btnplus.text()))
        btnplus.setStyleSheet('background: rgb{}; color: rgb{}; border: 3px dashed rgb{}'.format(self.color_button, self.text_color_2, self.border_color_2))
        btnplus.setFont(QFont('Arial', 13))

        btnminus = QPushButton('-')
        btnminus.clicked.connect(self.set_operation(btnminus.text()))
        btnminus.setStyleSheet('background: rgb{}; color: rgb{}; border: 3px dashed rgb{}'.format(self.color_button, self.text_color_2, self.border_color_2))
        btnminus.setFont(QFont('Arial', 13))

        btnmnozh = QPushButton('*')
        btnmnozh.clicked.connect(self.set_operation(btnmnozh.text()))
        btnmnozh.setStyleSheet('background: rgb{}; color: rgb{}; border: 3px dashed rgb{}'.format(self.color_button, self.text_color_2, self.border_color_2))
        btnmnozh.setFont(QFont('Arial', 13))

        btndelen = QPushButton('/')
        btndelen.clicked.connect(self.set_operation(btndelen.text()))
        btndelen.setStyleSheet('background: rgb{}; color: rgb{}; border: 3px dashed rgb{}'.format(self.color_button, self.text_color_2, self.border_color_2))
        btndelen.setFont(QFont('Arial', 13))

        btnproc = QPushButton('%')
        btnproc.clicked.connect(self.set_operation(btnproc.text()))
        btnproc.setStyleSheet('background: rgb{}; color: rgb{}; border: 3px dashed rgb{}'.format(self.color_button, self.text_color_2, self.border_color_2))
        btnproc.setFont(QFont('Arial', 13))

        btnstart = QPushButton('(')
        btnstart.clicked.connect(self.set_symbol(btnstart.text()))
        btnstart.setStyleSheet('background: rgb{}; color: rgb{}; border: 2px dashed rgb{}'.format(self.color_button_3, self.text_color_3, self.border_color_3))
        btnstart.setFont(QFont('Arial', 13))

        btnend = QPushButton(')')
        btnend.clicked.connect(self.set_symbol(btnend.text()))
        btnend.setStyleSheet('background: rgb{}; color: rgb{}; border: 2px dashed rgb{}'.format(self.color_button_3, self.text_color_3, self.border_color_3))
        btnend.setFont(QFont('Arial', 13))

        layout.addWidget(btnplus, 2, 3)
        layout.addWidget(btnminus, 3, 3)

        layout.addWidget(btnmnozh, 1, 0)
        layout.addWidget(btndelen, 1, 1)

        layout.addWidget(btnproc, 1, 2)

        btnDEL = QPushButton('DEL')
        btnDEL.clicked.connect(self.delfunct)
        layout.addWidget(btnDEL, 1, 3)
        btnDEL.setStyleSheet('background: rgb{}; color: rgb(255, 181, 181); border: 2px dashed rgb(110, 50, 50)'.format(self.color_button_2))
        btnDEL.setFont(QFont('Arial', 12))

        button = QPushButton('=')
        button.setStyleSheet('background: rgb{}; border-radius: 10px; border: 2px solid rgb{}; color: rgb{}'.format(self.color_button_3, self.border_color, self.text_color_3))
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(self.itog)
        button.setFont(QFont('Arial', 13))
        layout.addWidget(button, 4, 3, 2, 1)

        layout.addWidget(btnstart, 5, 0)
        layout.addWidget(btnend, 5, 1)

        btn0.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        btnplus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnminus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btndelen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnmnozh.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnproc.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnDEL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        btnstart.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btnend.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.setLayout(layout)

    # 1. считаем открывающие скобки: их не должно быть меньше, чем закрывающих

    def set_symbol(self, symbol):
        def button_clicked():
            output_text = self.text.text()
            last_symbol = output_text[-1]
            start_symbol = output_text[:-1]

            if last_symbol == '(' and symbol == ')' or start_symbol in self.not_number_operations or symbol == ')' and self.colvo_start == self.colvo_end:
                pass
            elif output_text == '0':
                output_text = symbol
                if symbol == '(':
                    self.colvo_start += 1
                if symbol == ')':
                    self.colvo_end += 1
            else:
                output_text += symbol
                if symbol == '(':
                    self.colvo_start += 1
                if symbol == ')':
                    self.colvo_end += 1
            self.text.setText(output_text)
        return button_clicked

    def set_operation(self, operation):
        def button_clicked():
            output_operation = self.text.text()  # весь текст
            last_symbol = output_operation[-1]  # ПОСЛЕДНИЙ символ

            # проверка
            # если послежний символ — открывающая скобка, можем поставить только минус
            if last_symbol == '(':
                if operation == '-':
                    output_operation += operation
            elif last_symbol in self.operations:  # если последний символ - это операция
                if len(output_operation) > 1:  # заменить минус в конструкции «(-» нельзя
                    last_last_symbol = output_operation[-2]
                    if last_last_symbol != '(':
                        output_operation = output_operation[:-1]
                        output_operation += operation
            else:  # если последний символ - цифра
                output_operation += operation
            self.text.setText(output_operation)
        return button_clicked

    def delfunct(self):
        output_text = self.text.text()
        if len(output_text) > 1:
            update = output_text[:-1]
        else:
            update = '0'
        self.text.setText(update)

    def itog(self):
        if self.colvo_start > self.colvo_end:
            print('Не закрыто скобок: {}'.format(self.colvo_start - self.colvo_end))
        elif self.colvo_end > self.colvo_start:
            print('Не открыто, но закрыто скобок: {}'.format(self.colvo_end - self.colvo_start))
        else:
            print('Все ок!')


app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
sys.exit(app.exec())
