# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import SSRWin
import GlintWin
import globalglintWin
import OptimalWin
import SensorControlWin



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        #MainWindow.hide()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 250)
        MainWindow.setMinimumSize(QtCore.QSize(1004, 250))
        MainWindow.setMaximumSize(QtCore.QSize(1004, 250))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 30, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 30, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(670, 30, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 130, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 130, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_1.clicked.connect(self.pushButton_1_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        self.pushButton_3.clicked.connect(self.pushButton_3_clicked)
        self.pushButton_4.clicked.connect(self.pushButton_4_clicked)
        self.pushButton_5.clicked.connect(self.pushButton_5_clicked)

    def pushButton_1_clicked(self):
        Win = SSRWin.MyMainWindow()
        Win.show()
    def pushButton_2_clicked(self):
        Win = GlintWin.MyMainWindow()
        Win.show()
    def pushButton_3_clicked(self):
        Win = globalglintWin.MyMainWindow()
        Win.show()
    def pushButton_4_clicked(self):
        Win = OptimalWin.MyMainWindow(self)
        Win.show()
    def pushButton_5_clicked(self):
        # Win = SensorControlWin.MyMainWindow()
        # Win.show()
        # Win = SSRWin.MyMainWindow()
        # Win.show()
        #app = QApplication(sys.argv)
        Win = SensorControlWin.MyMainWindow(self)
        Win.show()
        #sys.exit(app.exec())





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "Reverse SSR"))
        self.pushButton_2.setText(_translate("MainWindow", " Simulate SG radiance"))
        self.pushButton_3.setText(_translate("MainWindow", " Simulate SG radiance by location"))
        self.pushButton_4.setText(_translate("MainWindow", "Calculate optimal imaging angles"))
        self.pushButton_5.setText(_translate("MainWindow", "Calculate sensor parameters"))

