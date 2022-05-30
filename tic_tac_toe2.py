import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QFont, QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import *
import TicTacToe
import start
import random

my_list = []

class Start(QtWidgets.QMainWindow, start.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.evt_click_start_pvp)
        self.pushButton_2.clicked.connect(self.evt_click_start_ai)
        self.pvp_window = TicTacToeGame()
        self.ai_window = TicTacToeGameAI()


    def evt_click_start_pvp(self):
        self.hide()
        self.pvp_window.show()


    def evt_click_start_ai(self):
        self.hide()
        self.ai_window.show()

class ImgWidget1(QLabel):

    def __init__(self, parent=None):
        super(ImgWidget1, self).__init__(parent)
        pic = QtGui.QPixmap("pump.png")
        self.setPixmap(pic)

class ImgWidget2(QLabel):

    def __init__(self, parent=None):
        super(ImgWidget2, self).__init__(parent)
        pic = QtGui.QPixmap("fan.png")
        self.setPixmap(pic)


class TicTacToeGame(QtWidgets.QMainWindow, TicTacToe.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.evt_click)
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        self.label.setText('Игра Насосы - Вентиляторы')
        self.label.resize(400, 25)
        self.label_3.setText('Насосы')
        self.win_X = {}
        self.game_go = True
        self.my_row = 0
        self.my_column = 0
        grid = QGridLayout()
        for i in range(0, 3):
            for j in range(0, 3):
                self.tableWidget.setItem(i, j, QTableWidgetItem(''))

        self.count = 0

    def evt_click(self):
        self.item = ''
        if self.count % 2 == 0:
            self.label_3.setText('Вентиляторы')
            self.item = QTableWidgetItem('X')
            self.item.setFont(QFont('X', 1))
            self.tableWidget.setCellWidget(self.my_row, self.my_column, ImgWidget1(self))
            self.win_X[self.count] = (self.tableWidget.currentRow(), self.tableWidget.currentColumn())
            self.tableWidget.setItem(self.tableWidget.currentRow(), self.tableWidget.currentColumn(), self.item)
            if self.count > 3:
                if (self.tableWidget.item(0, 0).text() == 'X') and (
                        self.tableWidget.item(0, 1).text() == 'X') and (self.tableWidget.item(0, 2).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(1, 0).text() == 'X') and (self.tableWidget.item(1, 1).text() == 'X') and (
                        self.tableWidget.item(1, 2).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(2, 0).text() == 'X') and (self.tableWidget.item(2, 1).text() == 'X') and (
                        self.tableWidget.item(2, 2).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 0).text() == 'X') and (self.tableWidget.item(1, 0).text() == 'X') and (
                        self.tableWidget.item(2, 0).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 1).text() == 'X') and (self.tableWidget.item(1, 1).text() == 'X') and (
                        self.tableWidget.item(2, 1).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 2).text() == 'X') and (self.tableWidget.item(1, 2).text() == 'X') and (
                        self.tableWidget.item(2, 2).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 0).text() == 'X') and (self.tableWidget.item(1, 1).text() == 'X') and (
                        self.tableWidget.item(2, 2).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 2).text() == 'X') and (self.tableWidget.item(1, 1).text() == 'X') and (
                        self.tableWidget.item(2, 0).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                    self.label_5.resize(400, 25)

        else:
            self.label_3.setText('Насосы')
            self.item = QTableWidgetItem('O')
            self.item.setFont(QFont('O', 1))
            self.tableWidget.setCellWidget(self.my_row, self.my_column, ImgWidget2(self))

            self.item.setTextAlignment(4)
            self.win_X[self.count] = (self.tableWidget.currentRow(), self.tableWidget.currentColumn())
            # print(self.win_X)
            self.tableWidget.setItem(self.tableWidget.currentRow(), self.tableWidget.currentColumn(), self.item)
            if self.count > 3:
                if (self.tableWidget.item(0, 0).text() == 'O') and (self.tableWidget.item(0, 1).text() == 'O') and (
                        self.tableWidget.item(0, 2).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(1, 0).text() == 'O') and (self.tableWidget.item(1, 1).text() == 'O') and (
                        self.tableWidget.item(1, 2).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(2, 0).text() == 'O') and (self.tableWidget.item(2, 1).text() == 'O') and (
                        self.tableWidget.item(2, 2).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 0).text() == 'O') and (self.tableWidget.item(1, 0).text() == 'O') and (
                        self.tableWidget.item(2, 0).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 1).text() == 'O') and (self.tableWidget.item(1, 1).text() == 'O') and (
                        self.tableWidget.item(2, 1).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 2).text() == 'O') and (self.tableWidget.item(1, 2).text() == 'O') and (
                        self.tableWidget.item(2, 2).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 0).text() == 'O') and (self.tableWidget.item(1, 1).text() == 'O') and (
                        self.tableWidget.item(2, 2).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(2, 0).text() == 'O') and (self.tableWidget.item(1, 1).text() == 'O') and (
                        self.tableWidget.item(0, 2).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                    self.label_5.resize(400, 25)
        self.count += 1

    def win_game(self, marker):

        if self.count > 2:
            for i in range(0, 3):
                count = 0
                for j in range(0, 3):
                    if self.tableWidget.item(i, j).text() == marker:
                        count += 1
                    elif self.tableWidget.item(j, i).text() == marker:
                        count += 1
                    if count == 3:
                        print('win', marker)

    def cell_was_clicked(self, row, column):
        self.win_game('Насосы')
        self.win_game('Вентиляторы')
        self.my_row = self.tableWidget.item(row, column).row()
        self.my_column = self.tableWidget.item(row, column).column()

class TicTacToeGameAI(QtWidgets.QMainWindow, TicTacToe.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.evt_click)
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        self.label_3.setText('Насосы')
        self.win_X = {}
        self.game_go = True
        self.my_row = 0
        self.my_column = 0
        self.count = 0
        for i in range(0, 3):
            for j in range(0, 3):
                self.tableWidget.setItem(i, j, QTableWidgetItem(''))
                my_list.append([i,j])






    def evt_click(self):
        self.item = ''
        if self.count % 2 == 0:
            self.label_3.setText('Вентиляторы')
            self.item = QTableWidgetItem('X')
            self.item.setFont(QFont('X', 1))
            self.tableWidget.setCellWidget(self.my_row, self.my_column, ImgWidget1(self))
            my_list.remove([self.my_row, self.my_column])
            print(my_list)
            self.win_X[self.count] = (self.tableWidget.currentRow(), self.tableWidget.currentColumn())
            self.tableWidget.setItem(self.tableWidget.currentRow(), self.tableWidget.currentColumn(), self.item)
            if self.count > 3:
                if (self.tableWidget.item(0, 0).text() == 'X') and (self.tableWidget.item(0, 1).text() == 'X') and (
                        self.tableWidget.item(0, 2).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(1, 0).text() == 'X') and (self.tableWidget.item(1, 1).text() == 'X') and (
                        self.tableWidget.item(1, 2).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(2, 0).text() == 'X') and (self.tableWidget.item(2, 1).text() == 'X') and (
                        self.tableWidget.item(2, 2).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 0).text() == 'X') and (self.tableWidget.item(1, 0).text() == 'X') and (
                        self.tableWidget.item(2, 0).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 1).text() == 'X') and (self.tableWidget.item(1, 1).text() == 'X') and (
                        self.tableWidget.item(2, 1).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 2).text() == 'X') and (self.tableWidget.item(1, 2).text() == 'X') and (
                        self.tableWidget.item(2, 2).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 0).text() == 'X') and (self.tableWidget.item(1, 1).text() == 'X') and (
                        self.tableWidget.item(2, 2).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 2).text() == 'X') and (self.tableWidget.item(1, 1).text() == 'X') and (
                        self.tableWidget.item(2, 0).text() == 'X'):
                    self.label_5.setText('Насосы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                    self.label_5.resize(400, 25)

        self.count += 1
        print(self.count)

    def win_game(self, marker):

        if self.count > 2:
            for i in range(0, 3):
                count = 0
                for j in range(0, 3):
                    if self.tableWidget.item(i, j).text() == marker:
                        count += 1
                    elif self.tableWidget.item(j, i).text() == marker:
                        count += 1
                    if count == 3:
                        print('win', marker)

    def cell_was_clicked(self, row, column):
        self.win_game('Насосы')
        self.win_game('Вентиляторы')
        self.my_row = self.tableWidget.item(row, column).row()
        self.my_column = self.tableWidget.item(row, column).column()
        if self.count % 2 == 1:
            self.label_3.setText('Насосы')
            self.item = QTableWidgetItem('O')
            self.item.setFont(QFont('O', 1))
            ai_row = 0
            ai_column = 0
            while [ai_row, ai_column] not in my_list:
                ai_row = random.randint(0, 2)
                ai_column = random.randint(0, 2)
                print(ai_row, ai_column)

            self.tableWidget.setCellWidget(ai_row, ai_column, ImgWidget2(self))
            my_list.remove([ai_row, ai_column])

            self.item.setTextAlignment(4)
            self.win_X[self.count] = (self.tableWidget.currentRow(), self.tableWidget.currentColumn())
            # print(self.win_X)
            self.tableWidget.setItem(self.tableWidget.currentRow(), self.tableWidget.currentColumn(), self.item)
            if self.count > 3:
                if (self.tableWidget.item(0, 0).text() == 'O') and (self.tableWidget.item(0, 1).text() == 'O') and (
                        self.tableWidget.item(0, 2).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(1, 0).text() == 'O') and (self.tableWidget.item(1, 1).text() == 'O') and (
                        self.tableWidget.item(1, 2).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(2, 0).text() == 'O') and (self.tableWidget.item(2, 1).text() == 'O') and (
                        self.tableWidget.item(2, 2).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 0).text() == 'O') and (self.tableWidget.item(1, 0).text() == 'O') and (
                        self.tableWidget.item(2, 0).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 1).text() == 'O') and (self.tableWidget.item(1, 1).text() == 'O') and (
                        self.tableWidget.item(2, 1).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 2).text() == 'O') and (self.tableWidget.item(1, 2).text() == 'O') and (
                        self.tableWidget.item(2, 2).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(0, 0).text() == 'O') and (self.tableWidget.item(1, 1).text() == 'O') and (
                        self.tableWidget.item(2, 2).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                elif (self.tableWidget.item(2, 0).text() == 'O') and (self.tableWidget.item(1, 1).text() == 'O') and (
                        self.tableWidget.item(0, 2).text() == 'O'):
                    self.label_5.setText('Вентиляторы')
                    self.label_3.setText('')
                    self.pushButton_2.setEnabled(False)
                    
            self.count += 1


stylesheet = """
            start.Ui_MainWindow {
                background-image: url("C:/Users/DMalcev/PycharmProjects/pythonProject2/ris.jpg"); 
                background-repeat: no-repeat; 
                background-position: center;
            }
        """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("C:/Users/DMalcev/PycharmProjects/pythonProject2/ris.jpg")))
    Window = Start()
    Window.setPalette(palette)
    Window.show()
    sys.exit(app.exec())
