# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SSR2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import cv2

from PyQt5.QtWidgets import QDialog, QLabel

import Read_brs

import y_angle_calculate

from sun_zenith_azimuth import get_Sun_Zenith_Azimuth

from y_roughness_calculate import get_roughness

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Inversion_SSR(object):
    def setupUi(self, Inversion_SSR):
        Inversion_SSR.setObjectName("Inversion_SSR")
        Inversion_SSR.resize(1072, 743)
        Inversion_SSR.setMinimumSize(QtCore.QSize(1072, 743))
        Inversion_SSR.setMaximumSize(QtCore.QSize(1072, 743))
        self.centralwidget = QtWidgets.QWidget(Inversion_SSR)
        self.centralwidget.setObjectName("centralwidget")
        #标签Image 1
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 30, 111, 51))
        self.label.setObjectName("label")
        #选择Image 1的文件
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(340, 40, 271, 41))
        self.lineEdit_1.setObjectName("lineEdit")
        self.lineEdit_1.mouseDoubleClickEvent = self.lineEdit_1_double_click
        #标签Image2
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 120, 111, 51))
        self.label_2.setObjectName("label_2")
        #选择Image2文件
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 120, 271, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.mouseDoubleClickEvent = self.lineEdit_2_double_click
        #标签head File
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 200, 121, 51))
        self.label_3.setObjectName("label_3")
        #选择head File文件
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 200, 271, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.mouseDoubleClickEvent = self.lineEdit_3_double_click
        #标签Save Path
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 270, 121, 51))
        self.label_4.setObjectName("label_4")
        #选择 Save Path文件夹
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 270, 271, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.mouseDoubleClickEvent = self.lineEdit_4_double_click
        #标签save name
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 350, 121, 51))
        self.label_6.setObjectName("label_6")
        #填写保存文件名
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 350, 271, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.mouseDoubleClickEvent = self.lineEdit_5_double_click
        #Execute
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 640, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButton_clicked)
        #标签 Azimuth1
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(630, 40, 151, 51))
        self.label_7.setObjectName("label_7")
        #Azimuth1
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(790, 40, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        #标签Azimuth2
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(630, 110, 151, 51))
        self.label_8.setObjectName("label_8")
        #Azimuth2
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(790, 110, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        #标签Sensor parameter
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(210, 410, 221, 51))
        self.label_9.setObjectName("label_9")
        #标签IFOV
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 470, 111, 51))
        self.label_10.setObjectName("label_10")
        #IFOV,可能是表达式
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(320, 470, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        #标签Height
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(470, 460, 141, 51))
        self.label_11.setObjectName("label_11")
        #Height
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(610, 470, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        #标签Resolution
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(750, 460, 188, 51))
        self.label_12.setObjectName("label_12")
        #Resolution
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(945, 470, 128, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        #标签S
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(230, 530, 81, 51))
        self.label_13.setObjectName("label_13")
        #s
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(320, 530, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        #标签P
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(510, 530, 81, 51))
        self.label_14.setObjectName("label_14")
        #P
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(610, 530, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        #标签UTC
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(250, 590, 51, 51))
        self.label_15.setObjectName("label_15")
        #utc
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(320, 590, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")

        Inversion_SSR.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Inversion_SSR)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 23))
        self.menubar.setObjectName("menubar")
        Inversion_SSR.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Inversion_SSR)
        self.statusbar.setObjectName("statusbar")
        Inversion_SSR.setStatusBar(self.statusbar)

        self.retranslateUi(Inversion_SSR)
        QtCore.QMetaObject.connectSlotsByName(Inversion_SSR)

    def retranslateUi(self, Inversion_SSR):
        _translate = QtCore.QCoreApplication.translate
        Inversion_SSR.setWindowTitle(_translate("Inversion_SSR", "MainWindow"))
        self.label.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">Image 1:</span></p></body></html>"))
        self.label_2.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">Image 2:</span></p></body></html>"))
        self.label_3.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">Head File:</span></p></body></html>"))
        self.label_4.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">Save Path:</span></p></body></html>"))
        self.label_6.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">Save Name:</span></p></body></html>"))
        self.pushButton.setText(_translate("Inversion_SSR", "Execute"))
        self.label_7.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">Zenith1(°):</span></p></body></html>"))
        self.lineEdit_6.setText(_translate("Inversion_SSR", "0"))
        self.label_8.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">Zenith2(°):</span></p></body></html>"))
        self.lineEdit_7.setText(_translate("Inversion_SSR", "27.6"))
        self.label_9.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">Sensor parameter:</span></p></body></html>"))
        self.label_10.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">IFOV(rad):</span></p></body></html>"))
        self.lineEdit_8.setText(_translate("Inversion_SSR", "21.3*0.000001"))
        self.label_11.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">Height(km):</span></p></body></html>"))
        self.lineEdit_9.setText(_translate("Inversion_SSR", "705"))
        self.label_12.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">Resolution(m/n):</span></p></body></html>"))
        self.lineEdit_10.setText(_translate("Inversion_SSR", "15"))
        self.label_13.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">S(°):</span></p></body></html>"))
        self.label_14.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">P(°):</span></p></body></html>"))
        self.label_15.setText(_translate("Inversion_SSR", "<html><head/><body><p><span style=\" font-size:18pt;\">UTC:</span></p></body></html>"))

    def lineEdit_1_double_click(self, event):
        select_file = QtWidgets.QFileDialog.getOpenFileName(self, filter='*.tif')
        print(select_file)
        if select_file[0] != "":
            self.lineEdit_1.setText(select_file[0])
        else:
            self.lineEdit_1.setText(self.lineEdit_1.text())

    def lineEdit_2_double_click(self, event):
        select_file = QtWidgets.QFileDialog.getOpenFileName(self, filter='*.tif')
        print(select_file)
        if select_file[0] != "":
            self.lineEdit_2.setText(select_file[0])
        else:
            self.lineEdit_2.setText(self.lineEdit_2.text())

    def lineEdit_3_double_click(self, event):
        select_file = QtWidgets.QFileDialog.getOpenFileName(self, filter='*.brs')
        print(select_file)
        if select_file[0] != "":
            self.lineEdit_3.setText(select_file[0])
            utc_line, number, p, s = Read_brs.readFile(select_file[0])
            self.lineEdit_11.setText(s)
            self.lineEdit_12.setText(p)
            self.lineEdit_13.setText(utc_line)
            print(utc_line, number, p, s)
        else:
            self.lineEdit_3.setText(self.lineEdit_3.text())

    def lineEdit_4_double_click(self, event):
        select_file = QtWidgets.QFileDialog.getExistingDirectory(self)
        select_file = select_file.strip()
        if select_file != "":
            if select_file[-1] == "/":
                self.lineEdit_4.setText(select_file[:-1])
            else:
                self.lineEdit_4.setText(select_file)
        else:
            self.lineEdit_4.setText(self.lineEdit_4.text())

    def lineEdit_5_double_click(self, event):
        s1 = ""
        s2 = ""
        if self.lineEdit_1.text().strip() != "":
            s1 = self.lineEdit_1.text().strip().split("/")[-1].split(".")[0]
        if self.lineEdit_2.text().strip() != "":
            s2 = self.lineEdit_2.text().strip().split("/")[-1].split(".")[0]
        self.lineEdit_5.setText(s1 + "_" + s2 + "_" + "SSR.tif")

    def pushButton_clicked(self):
        self.target = True
        if self.lineEdit_1.text().strip() == "" or self.lineEdit_2.text().strip() == "" or\
                self.lineEdit_4.text().strip() == "" or self.lineEdit_5.text().strip() == "" \
                or self.lineEdit_6.text().strip() == ""  or self.lineEdit_7.text().strip() == "" \
                or self.lineEdit_8.text().strip() == ""  or self.lineEdit_9.text().strip() == "" \
                or self.lineEdit_10.text().strip() == ""  or self.lineEdit_11.text().strip() == "" \
                or self.lineEdit_12.text().strip() == ""  or self.lineEdit_13.text().strip() == "":
            self.showDialog_ok("Error", "Please check the information completion!")
        if not self.target:  # 用户确认检查数据的完整性，此时任务执行结束
            return
        print(self.target)
        image1 = self.lineEdit_1.text()
        image2 = self.lineEdit_2.text()
        img1 = cv2.imread(image1, -1)
        row1, col1 = img1.shape
        img2 = cv2.imread(image2, -1)
        row2, col2 = img2.shape
        del (img1)
        del (img2)
        if row1 != row2 or col1 != col2:
            self.showDialog_ok_cancel("Warn",
                                      "The size of image1 and image2 are different. " + "\n" + "Is it confirmed that the size is the smallest?")
        if not self.target:  # 如果数据尺寸不同，且用户不同意用最小尺寸，结束任务
            return
        col = min(col1,col2)
        row = min(row1,row2)
        p = float(self.lineEdit_12.text())
        s = float(self.lineEdit_11.text())
        zenith1 = float(self.lineEdit_6.text())
        zenith2 = float(self.lineEdit_7.text())
        ifov = float(eval(self.lineEdit_8.text()))
        H = float(self.lineEdit_9.text())
        M = float(self.lineEdit_10.text())
        utc = self.lineEdit_13.text()
        sun_zenith_azimuth = get_Sun_Zenith_Azimuth(image1,utc,col,row)
        image1_zenith, image1_azimuth, image2_zenith, image2_azimuth = y_angle_calculate.calculate(row,col,p,s,zenith1,zenith2,ifov,H,M)
        outpath = self.lineEdit_4.text().strip() + '\\' + self.lineEdit_5.text().strip()
        get_roughness(image1_zenith,image1_azimuth,image2_zenith,image2_azimuth,sun_zenith_azimuth,image1,image2,outpath,0,0,0,0)


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


    def showDialog_ok_cancel(self, title, message):
        self.dialog_2 = QDialog()
        self.dialog_2.setFixedSize(300, 100)
        pannel = QLabel(self.dialog_2)
        pannel.setText(message)
        pannel.move(10, 10)
        self.dialog_2.setWindowTitle(title)

        btn_ok = QtWidgets.QPushButton("ok", self.dialog_2)
        btn_ok.move(50, 50)
        btn_ok.clicked.connect(self.btn_ok_2)

        btn_cancel = QtWidgets.QPushButton("cancel", self.dialog_2)
        btn_cancel.move(200, 50)
        btn_cancel.clicked.connect(self.btn_cancel_2)

        self.dialog_2.exec_()


    def btn_ok_1(self):
        self.dialog_1.close()
        self.target = False

    def btn_ok_2(self):
        self.dialog_2.close()
        self.target = True

    def btn_cancel_2(self):
        self.dialog_2.close()
        self.target = False

