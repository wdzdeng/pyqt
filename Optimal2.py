# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Optimal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1313, 655)
        MainWindow.setMinimumSize(QtCore.QSize(1313, 655))
        MainWindow.setMaximumSize(QtCore.QSize(1313, 655))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 260, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(250, 80, 101, 41))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 80, 101, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 140, 101, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(370, 140, 101, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(250, 200, 101, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(370, 200, 101, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(250, 260, 101, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(370, 260, 101, 41))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 330, 433, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(480, 80, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(790, 80, 101, 41))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(790, 130, 101, 41))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(920, 80, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 140, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(790, 190, 101, 41))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(570, 190, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(1100, 80, 101, 41))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(910, 140, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(1100, 140, 101, 41))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(980, 200, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(1100, 200, 101, 41))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(60, 480, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(120, 480, 341, 41))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(60, 420, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(130, 420, 101, 41))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(270, 420, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(360, 420, 101, 41))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(490, 320, 401, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(920, 470, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1313, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.checkBox_1.toggled.connect(self.checkBox_1_change)
        self.checkBox_2.toggled.connect(self.checkBox_2_change)
        self.pushButton.clicked.connect(self.pushButton_clicked)
    def pushButton_clicked(self):
        sensor1_zenith_min = float(self.lineEdit_1.text().strip())
        sensor1_zenith_max = float(self.lineEdit_2.text().strip()) if float(self.lineEdit_2.text().strip())<90 else 89
        sensor1_Azimuth_min = float(self.lineEdit_3.text().strip())
        sensor1_Azimuth_max = float(self.lineEdit_4.text().strip())

        sensor2_zenith_min = float(self.lineEdit_5.text().strip())
        sensor2_zenith_max = float(self.lineEdit_6.text().strip()) if float(self.lineEdit_6.text().strip())<90 else 89
        sensor2_Azimuth_min = float(self.lineEdit_7.text().strip())
        sensor2_Azimuth_max = float(self.lineEdit_8.text().strip())

        if sensor1_zenith_max<sensor1_zenith_min or sensor1_Azimuth_max<sensor1_Azimuth_min or sensor2_zenith_max<sensor2_zenith_min or sensor2_Azimuth_max<sensor2_Azimuth_min:
            self.showDialog_ok("Error","Please confirm Max >= Min !",200,100)
            return
        location = [[sensor1_zenith_min,sensor1_zenith_max],[sensor1_Azimuth_min,sensor1_Azimuth_max],[sensor2_zenith_min,sensor2_zenith_max],[sensor2_Azimuth_min,],sensor2_Azimuth_max]
        point = int(self.lineEdit_16.text().strip())
        update = int(self.lineEdit_17.text().strip())

    def showDialog_ok(self, title, message, width, high):
        self.dialog_1 = QDialog()
        self.dialog_1.setFixedSize(width, high)
        pannel = QLabel(self.dialog_1)
        pannel.setText(message)
        pannel.move(10, 20)
        self.dialog_1.setWindowTitle(title)
        btn = QtWidgets.QPushButton("ok", self.dialog_1)
        btn.clicked.connect(self.btn_ok_1)
        btn.move(50, 50)
        self.dialog_1.exec_()

    def btn_ok_1(self):
        self.dialog_1.close()

    def checkBox_1_change(self):
        if self.checkBox_1.isChecked():
            self.lineEdit_3.setText("0")
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setText("0")
            self.lineEdit_4.setEnabled(False)
            if self.checkBox_2.isChecked():
                self.checkBox_2.setChecked(False)

        else:
            self.lineEdit_3.setText("")
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setText("")
            self.lineEdit_4.setEnabled(True)

    def checkBox_2_change(self):
        if self.checkBox_2.isChecked():
            self.lineEdit_7.setText("0")
            self.lineEdit_7.setEnabled(False)
            self.lineEdit_8.setText("0")
            self.lineEdit_8.setEnabled(False)
            if self.checkBox_1.isChecked():
                self.checkBox_1.setChecked(False)

        else:
            self.lineEdit_7.setText("")
            self.lineEdit_7.setEnabled(True)
            self.lineEdit_8.setText("")
            self.lineEdit_8.setEnabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sensor1 Zenith (°)"))
        self.label_2.setText(_translate("MainWindow", "Sensor1 Azimuth(°)"))
        self.label_3.setText(_translate("MainWindow", "Sensor2 Zenith(°)"))
        self.label_4.setText(_translate("MainWindow", "Sensor2 Azimuth(°)"))
        self.label_5.setText(_translate("MainWindow", "Min"))
        self.label_6.setText(_translate("MainWindow", "Max"))
        self.checkBox_1.setText(_translate("MainWindow", "Sensor1 Zenith = Sensor2 Zenith"))
        self.checkBox_2.setText(_translate("MainWindow", "Sensor1 Azimuth = Sensor2 Azimuth"))
        self.label_7.setText(_translate("MainWindow", "Sensor1 Multiply Error(%)"))
        self.label_9.setText(_translate("MainWindow", "Sun Zenith(°)"))
        self.label_10.setText(_translate("MainWindow", "Sensor2 Multiply Error(%)"))
        self.label_11.setText(_translate("MainWindow", "Sensor Add Error"))
        self.label_12.setText(_translate("MainWindow", "Sun Azimuth(°)"))
        self.label_13.setText(_translate("MainWindow", "Wind(m/s)"))
        self.label_14.setText(_translate("MainWindow", "UTC"))
        self.label_15.setText(_translate("MainWindow", "Point"))
        self.lineEdit_16.setText(_translate("MainWindow", "10000"))
        self.label_16.setText(_translate("MainWindow", "Update"))
        self.lineEdit_17.setText(_translate("MainWindow", "200"))
        self.pushButton.setText(_translate("MainWindow", "Execute"))


