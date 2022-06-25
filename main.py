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

        layout = QGridLayout()

        #цифры
        self.text = QtWidgets.QLabel(self)
        self.text.setText('0')
        self.text.setFont(QFont('Arial', 13))

        layout.addWidget(self.text, 0, 0, 1, 4, alignment=Qt.AlignRight)

        btn7 = QPushButton('7')
        btn7.clicked.connect(self.set_symbol(btn7.text()))
        btn8 = QPushButton('8')
        btn8.clicked.connect(self.set_symbol(btn8.text()))
        btn9 = QPushButton('9')
        btn9.clicked.connect(self.set_symbol(btn9.text()))

        btn4 = QPushButton('4')
        btn4.clicked.connect(self.set_symbol(btn4.text()))
        btn5 = QPushButton('5')
        btn5.clicked.connect(self.set_symbol(btn5.text()))
        btn6 = QPushButton('6')
        btn6.clicked.connect(self.set_symbol(btn6.text()))

        btn1 = QPushButton('1')
        btn1.clicked.connect(self.set_symbol(btn1.text()))
        btn2 = QPushButton('2')
        btn2.clicked.connect(self.set_symbol(btn2.text()))
        btn3 = QPushButton('3')
        btn3.clicked.connect(self.set_symbol(btn3.text()))

        btn0 = QPushButton('0')
        btn0.clicked.connect(self.set_symbol(btn0.text()))

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
        operations = ['+', '-', '*', '/', '%']

        btnplus = QPushButton('+')
        btnplus.clicked.connect(self.set_symbol(btnplus.text()))
        btnminus = QPushButton('-')
        btnminus.clicked.connect(self.set_operation(btnminus.text()))

        btnmnozh = QPushButton('*')
        btnmnozh.clicked.connect(self.set_symbol(btnmnozh.text()))
        btndelen = QPushButton('/')
        btndelen.clicked.connect(self.set_symbol(btndelen.text()))

        btnproc = QPushButton('%')
        btnproc.clicked.connect(self.set_symbol(btnproc.text()))

        btnstart = QPushButton('(')
        btnstart.clicked.connect(self.set_symbol(btnstart.text()))
        btnend = QPushButton(')')
        btnend.clicked.connect(self.set_symbol(btnend.text()))

        layout.addWidget(btnplus, 2, 3)
        layout.addWidget(btnminus, 3, 3)

        layout.addWidget(btnmnozh, 1, 0)
        layout.addWidget(btndelen, 1, 1)

        layout.addWidget(btnproc, 1, 2)

        layout.addWidget(QPushButton('DEL'), 1, 3)

        self.button = QPushButton('=')
        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.button, 4, 3, 2, 1)

        layout.addWidget(btnstart, 5, 0)
        layout.addWidget(btnend, 5, 1)

        self.setLayout(layout)

    def set_symbol(self, symbol):
        def button_clicked():
            output_text = self.text.text()
            if output_text == '0':
                output_text = symbol
            else:
                output_text += symbol
            self.text.setText(output_text)
        return button_clicked

    def set_operation(self, operation):
        def button_clicked():
            output_operation = self.text.text() #весь текст
            last_symbol = output_operation[-1] #ПОСЛЕДНИЙ символ
            print('до проверки')

            #проверка
            if last_symbol == '+': #если последний символ - это +
                print('проверка на операцию')
                output_operation -= last_symbol#вычитается последний символ
                output_operation += operation#прибавляется операция
            else:#если последний символ - цифра
                print('другое на число')
                output_operation += operation#просто прибавляется операция
            self.text.setText(output_operation)
        return button_clicked


app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
sys.exit(app.exec())
