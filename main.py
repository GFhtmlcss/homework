import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout


class Display(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('homework layout')
        self.setGeometry(150, 150, 1000, 400)

        #первое дз. статус: баги: текст не по середине
        # self.text = QtWidgets.QLabel(self)
        # self.text.setText('Млекопитающие с самыми большими ушами - слоны?')
        #
        # layoutText = QHBoxLayout()
        # layoutText.addWidget(self.text, alignment=Qt.AlignCenter)
        # layoutH = QHBoxLayout()
        # layoutH.addWidget(QPushButton('да!'), alignment=Qt.AlignBottom)
        # layoutH.addWidget(QPushButton('нет!'), alignment=Qt.AlignBottom)
        #
        # layoutText.addLayout(layoutH)
        # self.setLayout(layoutText)


        # второе дз. статус: НЕ СДЕЛАНО
        # layout= QHBoxLayout()
        # layoutpicture = QVBoxLayout()
        # layout.addWidget(QPushButton('папка'), alignment=Qt.AlignTop)
        #
        # layoutpicture.addWidget(QPushButton('картинка'))
        # layout.addLayout(layoutpicture)
        #
        # layout.addWidget(QPushButton('лево'), alignment=Qt.AlignBottom)
        # layout.addWidget(QPushButton('право'), alignment=Qt.AlignBottom)
        # layout.addWidget(QPushButton('зеркало'), alignment=Qt.AlignBottom)
        # layout.addWidget(QPushButton('резкость'), alignment=Qt.AlignBottom)
        # layout.addWidget(QPushButton('ч/б'), alignment=Qt.AlignBottom)
        #
        # self.setLayout(layout)


        #третье дз.  статус: ПОЛНОСТЬЮ ВЫПОЛНЕНО
        layout = QGridLayout()
        #
        # layout.addWidget(QPushButton('00'), 0, 0)
        # layout.addWidget(QPushButton('01'), 0, 1)
        # layout.addWidget(QPushButton('02'), 0, 2)
        # layout.addWidget(QPushButton('03'), 0, 3)
        # layout.addWidget(QPushButton('04'), 0, 4)
        #
        # layout.addWidget(QPushButton('10'), 1, 0)
        # layout.addWidget(QPushButton('11'), 1, 1)
        # layout.addWidget(QPushButton('12'), 1, 2)
        # layout.addWidget(QPushButton('13'), 1, 3)
        # layout.addWidget(QPushButton('14'), 1, 4)
        #
        # layout.addWidget(QPushButton('20'), 2, 0)
        # layout.addWidget(QPushButton('21'), 2, 1)
        # layout.addWidget(QPushButton('22'), 2, 2)
        # layout.addWidget(QPushButton('23'), 2, 3)
        # layout.addWidget(QPushButton('24'), 2, 4)
        #
        # layout.addWidget(QPushButton('30'), 3, 0)
        # layout.addWidget(QPushButton('31'), 3, 1)
        # layout.addWidget(QPushButton('32'), 3, 2)
        # layout.addWidget(QPushButton('33'), 3, 3)
        # layout.addWidget(QPushButton('34'), 3, 4)
        #
        # layout.addWidget(QPushButton('40'), 4, 0)
        # layout.addWidget(QPushButton('41'), 4, 1)
        # layout.addWidget(QPushButton('42'), 4, 2)
        # layout.addWidget(QPushButton('43'), 4, 3)
        # layout.addWidget(QPushButton('44'), 4, 4)

        whilecheck = 0
        num_1 = 0
        num_2 = 0
        number = str(whilecheck)
        while whilecheck < 45:
            layout.addWidget(QPushButton(number), num_1, num_2)
            whilecheck += 1
            number = str(whilecheck)
            num_2 += 1
            if whilecheck % 5 == 0:
                whilecheck += 5
                number = str(whilecheck)
                num_1 += 1
                num_2 = 0

        self.setLayout(layout)

app = QApplication(sys.argv)
display = Display()
display.show()
sys.exit(app.exec())
