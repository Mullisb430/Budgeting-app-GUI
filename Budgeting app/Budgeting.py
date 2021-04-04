#!/Users/brandonmullis/opt/anaconda3/bin/python
import sys
from typing import Counter
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from saveFile import *
import random


class Test(QMainWindow):
    def __init__(self):
        super(Test, self).__init__()
        loadUi('Budgeting.ui', self)
        self.itemValue.textChanged.connect(self.calculate)
        self.itemValue2.textChanged.connect(self.calculate)
        self.itemValue3.textChanged.connect(self.calculate)
        self.itemValue4.textChanged.connect(self.calculate)
        self.itemValue5.textChanged.connect(self.calculate)
        self.itemValue6.textChanged.connect(self.calculate)
        self.itemValue7.textChanged.connect(self.calculate)
        self.itemValue8.textChanged.connect(self.calculate)
        self.itemValue9.textChanged.connect(self.calculate)
        self.itemValue10.textChanged.connect(self.calculate)
        self.itemValue11.textChanged.connect(self.calculate)
        self.itemValue12.textChanged.connect(self.calculate)
        self.itemValue13.textChanged.connect(self.calculate)
        self.itemValue14.textChanged.connect(self.calculate)
        self.itemValue15.textChanged.connect(self.calculate)
        self.itemValue16.textChanged.connect(self.calculate)
        self.itemValue17.textChanged.connect(self.calculate)
        self.salaryValue.textChanged.connect(self.calculate)
        self.itemValue.textChanged.connect(self.color)
        self.itemValue2.textChanged.connect(self.color)
        self.itemValue3.textChanged.connect(self.color)
        self.itemValue4.textChanged.connect(self.color)
        self.itemValue5.textChanged.connect(self.color)
        self.itemValue6.textChanged.connect(self.color)
        self.itemValue7.textChanged.connect(self.color)
        self.itemValue8.textChanged.connect(self.color)
        self.itemValue9.textChanged.connect(self.color)
        self.itemValue10.textChanged.connect(self.color)
        self.itemValue11.textChanged.connect(self.color)
        self.itemValue12.textChanged.connect(self.color)
        self.itemValue13.textChanged.connect(self.color)
        self.itemValue14.textChanged.connect(self.color)
        self.itemValue15.textChanged.connect(self.color)
        self.itemValue16.textChanged.connect(self.color)
        self.itemValue17.textChanged.connect(self.color)
        self.salaryValue.textChanged.connect(self.color)
        self.bootLoad()
        self.loadButton.clicked.connect(self.load)
        self.saveButton.clicked.connect(self.save)

    def bootLoad(self):
        self.itemName.setText(item1)
        self.itemValue.setText(value1)
        self.itemName2.setText(item2)
        self.itemValue2.setText(value2)
        self.itemName3.setText(item3)
        self.itemValue3.setText(value3)
        self.itemName4.setText(item4)
        self.itemValue4.setText(value4)
        self.itemName5.setText(item5)
        self.itemValue5.setText(value5)
        self.itemName6.setText(item6)
        self.itemValue6.setText(value6)
        self.itemName7.setText(item7)
        self.itemValue7.setText(value7)
        self.itemName8.setText(item8)
        self.itemValue8.setText(value8)
        self.itemName9.setText(item9)
        self.itemValue9.setText(value9)
        self.itemName10.setText(item10)
        self.itemValue10.setText(value10)
        self.itemName11.setText(item11)
        self.itemValue11.setText(value11)
        self.itemName12.setText(item12)
        self.itemValue12.setText(value12)
        self.itemName13.setText(item13)
        self.itemValue13.setText(value13)
        self.itemName14.setText(item14)
        self.itemValue14.setText(value14)
        self.itemName15.setText(item15)
        self.itemValue15.setText(value15)
        self.itemName16.setText(item16)
        self.itemValue16.setText(value16)
        self.itemName17.setText(item17)
        self.itemValue17.setText(value17)
        self.salaryValue.setText(salary)

    def save(self):
        with open('saveFile.py', 'w') as file:
            file.write(f'item1 = \'{self.itemName.text()}\'\nvalue1 = \'{self.itemValue.text()}\'\n')
            file.write(f'item2 = \'{self.itemName2.text()}\'\nvalue2 = \'{self.itemValue2.text()}\'\n')
            file.write(f'item3 = \'{self.itemName3.text()}\'\nvalue3 = \'{self.itemValue3.text()}\'\n')
            file.write(f'item4 = \'{self.itemName4.text()}\'\nvalue4 = \'{self.itemValue4.text()}\'\n')
            file.write(f'item5 = \'{self.itemName5.text()}\'\nvalue5 = \'{self.itemValue5.text()}\'\n')
            file.write(f'item6 = \'{self.itemName6.text()}\'\nvalue6 = \'{self.itemValue6.text()}\'\n')
            file.write(f'item7 = \'{self.itemName7.text()}\'\nvalue7 = \'{self.itemValue7.text()}\'\n')
            file.write(f'item8 = \'{self.itemName8.text()}\'\nvalue8 = \'{self.itemValue8.text()}\'\n')
            file.write(f'item9 = \'{self.itemName9.text()}\'\nvalue9 = \'{self.itemValue9.text()}\'\n')
            file.write(f'item10 = \'{self.itemName10.text()}\'\nvalue10 = \'{self.itemValue10.text()}\'\n')
            file.write(f'item11 = \'{self.itemName11.text()}\'\nvalue11 = \'{self.itemValue11.text()}\'\n')
            file.write(f'item12 = \'{self.itemName12.text()}\'\nvalue12 = \'{self.itemValue12.text()}\'\n')
            file.write(f'item13 = \'{self.itemName13.text()}\'\nvalue13 = \'{self.itemValue13.text()}\'\n')
            file.write(f'item14 = \'{self.itemName14.text()}\'\nvalue14 = \'{self.itemValue14.text()}\'\n')
            file.write(f'item15 = \'{self.itemName15.text()}\'\nvalue15 = \'{self.itemValue15.text()}\'\n')
            file.write(f'item16 = \'{self.itemName16.text()}\'\nvalue16 = \'{self.itemValue16.text()}\'\n')
            file.write(f'item17 = \'{self.itemName17.text()}\'\nvalue17 = \'{self.itemValue17.text()}\'\n')
            file.write(f'salary = \'{self.salaryValue.text()}\'')
            file.close()

    def load(self):
        self.itemName.setText(item1)
        self.itemValue.setText(value1)
        self.itemName2.setText(item2)
        self.itemValue2.setText(value2)
        self.itemName3.setText(item3)
        self.itemValue3.setText(value3)
        self.itemName4.setText(item4)
        self.itemValue4.setText(value4)
        self.itemName5.setText(item5)
        self.itemValue5.setText(value5)
        self.itemName6.setText(item6)
        self.itemValue6.setText(value6)
        self.itemName7.setText(item7)
        self.itemValue7.setText(value7)
        self.itemName8.setText(item8)
        self.itemValue8.setText(value8)
        self.itemName9.setText(item9)
        self.itemValue9.setText(value9)
        self.itemName10.setText(item10)
        self.itemValue10.setText(value10)
        self.itemName11.setText(item11)
        self.itemValue11.setText(value11)
        self.itemName12.setText(item12)
        self.itemValue12.setText(value12)
        self.itemName13.setText(item13)
        self.itemValue13.setText(value13)
        self.itemName14.setText(item14)
        self.itemValue14.setText(value14)
        self.itemName15.setText(item15)
        self.itemValue15.setText(value15)
        self.itemName16.setText(item16)
        self.itemValue16.setText(value16)
        self.itemName17.setText(item17)
        self.itemValue17.setText(value17)
        self.salaryValue.setText(salary)

        
    
    def calculate(self):
        try:
            total = [float(self.itemValue.text()), float(self.itemValue2.text()), float(self.itemValue3.text()), float(self.itemValue4.text()), float(self.itemValue5.text()), float(self.itemValue6.text()), float(self.itemValue7.text()), float(self.itemValue8.text()), float(self.itemValue9.text()), float(self.itemValue10.text()), float(self.itemValue11.text()), float(self.itemValue12.text()), float(self.itemValue13.text()), float(self.itemValue14.text()), float(self.itemValue15.text()), float(self.itemValue16.text()), float(self.itemValue17.text())]
        except Exception:
            total = [0, 0]

        try:
            self.total.setText(str(round(sum(total), 2)))
        except Exception:
            self.total.setText(str(0))

        try:
            self.net.setText(str(round(float(self.salaryValue.text()) - sum(total), 2)))
        except Exception:
            self.net.setText(str(0))

    def color(self):
        if float(self.net.text()) < 0:
            self.net.setStyleSheet("QLabel { color: #ff0000; font: 40pt \".AppleSystemUIFont\" }")
        else:
            self.net.setStyleSheet("QLabel { color: #00ff00; font: 40pt \".AppleSystemUIFont\" }")


        

app = QApplication(sys.argv)
test = Test()
test.setFixedSize(749, 458)
test.show()
app.exec()