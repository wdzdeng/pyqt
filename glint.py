# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glint2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1410, 879)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 90, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(480, 90, 121, 41))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 150, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 150, 121, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 210, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(480, 210, 121, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 270, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(480, 270, 121, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 340, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(480, 340, 121, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 60, 50, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.radioButton_1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_1.setText("")
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_1.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_5.setText("")
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout.addWidget(self.radioButton_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 60, 50, 351))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_6.setText("")
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_7.setText("")
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout_2.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_8.setText("")
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout_2.addWidget(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_9.setText("")
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout_2.addWidget(self.radioButton_9)
        self.radioButton_10 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_10.setText("")
        self.radioButton_10.setObjectName("radioButton_10")
        self.verticalLayout_2.addWidget(self.radioButton_10)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(610, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(690, 90, 121, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(840, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(890, 90, 121, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1040, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(1110, 90, 121, 41))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(610, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(690, 160, 121, 41))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(840, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(890, 160, 121, 41))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1040, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(1110, 160, 121, 41))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(840, 220, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(610, 220, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(690, 220, 121, 41))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1040, 220, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(1110, 220, 121, 41))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(890, 220, 121, 41))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(840, 280, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(610, 280, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(690, 280, 121, 41))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1040, 280, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(1110, 280, 121, 41))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(890, 280, 121, 41))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(840, 350, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(610, 350, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(690, 350, 121, 41))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(1040, 350, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setGeometry(QtCore.QRect(1110, 340, 121, 41))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_20.setGeometry(QtCore.QRect(890, 340, 121, 41))
        self.lineEdit_20.setObjectName("lineEdit_20")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1410, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.xmap = {self.radioButton_1:[self.label_8,self.lineEdit_6,self.label_9,self.lineEdit_7,self.label_10,self.lineEdit_8], \

                    self.radioButton_2: [self.label_11, self.lineEdit_9, self.label_12, self.lineEdit_10, self.label_13,self.lineEdit_11], \

                    self.radioButton_3: [self.label_15, self.lineEdit_12, self.label_14, self.lineEdit_14, self.label_16,self.lineEdit_13], \

                    self.radioButton_4: [self.label_18, self.lineEdit_15, self.label_17, self.lineEdit_17, self.label_19, self.lineEdit_16], \

                    self.radioButton_5: [self.label_21, self.lineEdit_18, self.label_20, self.lineEdit_20,self.label_22, self.lineEdit_19], \

                    }
        self.multmap = {
            self.radioButton_6: [self.label_8, self.lineEdit_6, self.label_9, self.lineEdit_7, self.label_10, self.lineEdit_8], \
            self.radioButton_7: [self.label_11, self.lineEdit_9, self.label_12, self.lineEdit_10, self.label_13,self.lineEdit_11], \
            self.radioButton_8: [self.label_15, self.lineEdit_12, self.label_14, self.lineEdit_14, self.label_16,self.lineEdit_13], \
            self.radioButton_9: [self.label_18, self.lineEdit_15, self.label_17, self.lineEdit_17, self.label_19,self.lineEdit_16], \
            self.radioButton_10: [self.label_21, self.lineEdit_18, self.label_20, self.lineEdit_20, self.label_22,self.lineEdit_19], \
            }
        self.mult_X_map = {
            self.radioButton_1:self.radioButton_6,self.radioButton_6:self.radioButton_1, \
            self.radioButton_2: self.radioButton_7, self.radioButton_7: self.radioButton_2, \
            self.radioButton_3: self.radioButton_8, self.radioButton_8: self.radioButton_3, \
            self.radioButton_4: self.radioButton_9, self.radioButton_9: self.radioButton_4, \
            self.radioButton_5: self.radioButton_10, self.radioButton_10: self.radioButton_5,
            }

        self.attributemap = {
            "satellite_zenith":[self.lineEdit_1,self.lineEdit_6,self.lineEdit_7,self.lineEdit_8], \
            "satellite_azimuth": [self.lineEdit_2, self.lineEdit_9, self.lineEdit_10, self.lineEdit_11], \
            "sun_zenith": [self.lineEdit_3, self.lineEdit_12, self.lineEdit_14, self.lineEdit_13], \
            "sun_azimuth": [self.lineEdit_4, self.lineEdit_15, self.lineEdit_17, self.lineEdit_16], \
            "feng": [self.lineEdit_5, self.lineEdit_18, self.lineEdit_20, self.lineEdit_19], \
            }

        self.initial_visualization()
        self.radioButton_1.toggled.connect(self.radioButton_1_change)
        self.radioButton_2.toggled.connect(self.radioButton_2_change)
        self.radioButton_3.toggled.connect(self.radioButton_3_change)
        self.radioButton_4.toggled.connect(self.radioButton_4_change)
        self.radioButton_5.toggled.connect(self.radioButton_5_change)
        self.radioButton_6.toggled.connect(self.radioButton_6_change)
        self.radioButton_7.toggled.connect(self.radioButton_7_change)
        self.radioButton_8.toggled.connect(self.radioButton_8_change)
        self.radioButton_9.toggled.connect(self.radioButton_9_change)
        self.radioButton_10.toggled.connect(self.radioButton_10_change)


    def initial_visualization(self):
        radioButtonList = self.xmap.keys()
        self.lineEdit_1.setEnabled(False)
        for radiobuttion in radioButtonList:
            print(radiobuttion)
            if radiobuttion.isChecked():
                self.mult_X_map[radiobuttion].setEnabled(False)
                for lableOrLineEdit in self.xmap[radiobuttion]:
                    lableOrLineEdit.setVisible(True)
            else:
                for lableOrLineEdit in self.xmap[radiobuttion]:
                    lableOrLineEdit.setVisible(False)

    def radioButton_1_change(self):
        if self.radioButton_1.isChecked():
            self.mult_X_map[self.radioButton_1].setEnabled(False)
            self.lineEdit_1.setEnabled(False)
            for lableOrLineEdit in self.xmap[self.radioButton_1]:
                lableOrLineEdit.setVisible(True)
        else:
            self.mult_X_map[self.radioButton_1].setEnabled(True)
            self.lineEdit_1.setEnabled(True)
            for lableOrLineEdit in self.xmap[self.radioButton_1]:
                lableOrLineEdit.setVisible(False)

    def radioButton_2_change(self):
        if self.radioButton_2.isChecked():
            self.lineEdit_2.setEnabled(False)
            self.mult_X_map[self.radioButton_2].setEnabled(False)
            for lableOrLineEdit in self.xmap[self.radioButton_2]:
                lableOrLineEdit.setVisible(True)
        else:
            self.lineEdit_2.setEnabled(True)
            self.mult_X_map[self.radioButton_2].setEnabled(True)
            for lableOrLineEdit in self.xmap[self.radioButton_2]:
                lableOrLineEdit.setVisible(False)

    def radioButton_3_change(self):
        if self.radioButton_3.isChecked():
            self.lineEdit_3.setEnabled(False)
            self.mult_X_map[self.radioButton_3].setEnabled(False)
            for lableOrLineEdit in self.xmap[self.radioButton_3]:
                lableOrLineEdit.setVisible(True)
        else:
            self.lineEdit_3.setEnabled(True)
            self.mult_X_map[self.radioButton_3].setEnabled(True)
            for lableOrLineEdit in self.xmap[self.radioButton_3]:
                lableOrLineEdit.setVisible(False)

    def radioButton_4_change(self):
        if self.radioButton_4.isChecked():
            self.lineEdit_4.setEnabled(False)
            self.mult_X_map[self.radioButton_4].setEnabled(False)
            for lableOrLineEdit in self.xmap[self.radioButton_4]:
                lableOrLineEdit.setVisible(True)
        else:
            self.lineEdit_4.setEnabled(True)
            self.mult_X_map[self.radioButton_4].setEnabled(True)
            for lableOrLineEdit in self.xmap[self.radioButton_4]:
                lableOrLineEdit.setVisible(False)

    def radioButton_5_change(self):
        if self.radioButton_5.isChecked():
            self.lineEdit_5.setEnabled(False)
            self.mult_X_map[self.radioButton_5].setEnabled(False)
            for lableOrLineEdit in self.xmap[self.radioButton_5]:
                lableOrLineEdit.setVisible(True)
        else:
            self.lineEdit_5.setEnabled(True)
            self.mult_X_map[self.radioButton_5].setEnabled(True)
            for lableOrLineEdit in self.xmap[self.radioButton_5]:
                lableOrLineEdit.setVisible(False)

    def radioButton_6_change(self):
        if self.radioButton_6.isChecked():
            self.mult_X_map[self.radioButton_6].setEnabled(False)
            for lableOrLineEdit in self.multmap[self.radioButton_6]:
                lableOrLineEdit.setVisible(True)
        else:
            self.mult_X_map[self.radioButton_6].setEnabled(True)
            for lableOrLineEdit in self.multmap[self.radioButton_6]:
                lableOrLineEdit.setVisible(False)

    def radioButton_7_change(self):
        if self.radioButton_7.isChecked():
            self.mult_X_map[self.radioButton_7].setEnabled(False)
            for lableOrLineEdit in self.multmap[self.radioButton_7]:
                lableOrLineEdit.setVisible(True)
        else:
            self.mult_X_map[self.radioButton_7].setEnabled(True)
            for lableOrLineEdit in self.multmap[self.radioButton_7]:
                lableOrLineEdit.setVisible(False)

    def radioButton_8_change(self):
        if self.radioButton_8.isChecked():
            self.mult_X_map[self.radioButton_8].setEnabled(False)
            for lableOrLineEdit in self.multmap[self.radioButton_8]:
                lableOrLineEdit.setVisible(True)
        else:
            self.mult_X_map[self.radioButton_8].setEnabled(True)
            for lableOrLineEdit in self.multmap[self.radioButton_8]:
                lableOrLineEdit.setVisible(False)

    def radioButton_9_change(self):
        if self.radioButton_9.isChecked():
            self.mult_X_map[self.radioButton_9].setEnabled(False)
            for lableOrLineEdit in self.multmap[self.radioButton_9]:
                lableOrLineEdit.setVisible(True)
        else:
            self.mult_X_map[self.radioButton_9].setEnabled(True)
            for lableOrLineEdit in self.multmap[self.radioButton_9]:
                lableOrLineEdit.setVisible(False)

    def radioButton_10_change(self):
        if self.radioButton_10.isChecked():
            self.mult_X_map[self.radioButton_10].setEnabled(False)
            for lableOrLineEdit in self.multmap[self.radioButton_10]:
                lableOrLineEdit.setVisible(True)
        else:
            self.mult_X_map[self.radioButton_10].setEnabled(True)
            for lableOrLineEdit in self.multmap[self.radioButton_10]:
                lableOrLineEdit.setVisible(False)

    def showDialog_ok(self, title, message):
        self.dialog_1 = QDialog()
        self.dialog_1.setFixedSize(300, 100)
        pannel = QLabel(self.dialog_1)
        pannel.setText(message)
        pannel.move(30, 20)
        self.dialog_1.setWindowTitle(title)
        btn = QtWidgets.QPushButton("ok", self.dialog_1)
        btn.clicked.connect(self.btn_ok_1)
        btn.move(100, 50)
        self.dialog_1.exec_()
    def btn_ok_1(self):
        self.radioButton_6.setChecked(False)
        self.dialog_1.close()





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Satellite zenith(°):</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Satellite azimuth(°):</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Sun zenith(°):</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Sun azimuth(°)</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Wind(m/s)</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "   X"))
        self.label_7.setText(_translate("MainWindow", "Multi"))
        self.label_8.setText(_translate("MainWindow", "From"))
        self.label_9.setText(_translate("MainWindow", "To"))
        self.label_10.setText(_translate("MainWindow", "Step"))
        self.label_11.setText(_translate("MainWindow", "From"))
        self.label_12.setText(_translate("MainWindow", "To"))
        self.label_13.setText(_translate("MainWindow", "Step"))
        self.label_14.setText(_translate("MainWindow", "To"))
        self.label_15.setText(_translate("MainWindow", "From"))
        self.label_16.setText(_translate("MainWindow", "Step"))
        self.label_17.setText(_translate("MainWindow", "To"))
        self.label_18.setText(_translate("MainWindow", "From"))
        self.label_19.setText(_translate("MainWindow", "Step"))
        self.label_20.setText(_translate("MainWindow", "To"))
        self.label_21.setText(_translate("MainWindow", "From"))
        self.label_22.setText(_translate("MainWindow", "Step"))

