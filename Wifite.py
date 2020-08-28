#!/usr/bin/env python

# Note: This script runs Wifite from within a cloned git repo.
# The script `bin/wifite` is designed to be run after installing (from /usr/sbin), not from the cwd.
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from wifite import __main__

class Depart():

    def setupUi(self, win):
        win.setObjectName("MainWindow")
        win.setFixedSize(930, 670)
        win.setStyleSheet("background-color: white")
        self.start_crack = QtWidgets.QPushButton(win)
        self.start_crack.setText("Start wifi cracking")
        self.start_crack.setGeometry(266, 230, 390, 70)
        self.start_crack.setFont(QtGui.QFont("Funkturm", 11))
        self.start_crack.setStyleSheet("background-color: #EDFEFF;border-style: outset;border-width: 2px;border-radius: 15px;border-color: black;padding: 4px;")
        self.start_crack.clicked.connect(lambda: __main__.entry_point())




app = QtWidgets.QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("Menu")

ui = Depart()
ui.setupUi(win)

win.show()
sys.exit(app.exec_())
