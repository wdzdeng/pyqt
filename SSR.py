# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SSR2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import cv2
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QDialog, QLabel, QProgressBar, QPushButton

import Read_brs

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Inversion_SSR(object):
    def setupUi(self, Inversion_SSR):
        Inversion_SSR.setObjectName("Inversion_SSR")
        Inversion_SSR.resize(1072, 743)
        Inversion_SSR.setMinimumSize(QtCore.QSize(1072, 743))
        Inversion_SSR.setMaximumSize(QtCore.QSize(1072, 743))
        self.centralwidget = QtWidgets.QWidget(Inversion_SSR)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 110, 111, 51))
        self.label.setObjectName("label")

        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(450, 120, 271, 41))
        self.lineEdit_1.setObjectName("lineEdit")
        self.lineEdit_1.mouseDoubleClickEvent=self.lineEdit_1_double_click

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 200, 111, 51))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 200, 271, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.mouseDoubleClickEvent = self.lineEdit_2_double_click

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 290, 121, 51))
        self.label_3.setObjectName("label_3")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(450, 290, 271, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.mouseDoubleClickEvent = self.lineEdit_3_double_click

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 370, 121, 51))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 330, 271, 31))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(450, 370, 271, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.mouseDoubleClickEvent = self.lineEdit_4_double_click

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 440, 121, 51))
        self.label_6.setObjectName("label_6")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(450, 440, 271, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.mouseDoubleClickEvent = self.lineEdit_5_double_click

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 530, 121, 51))
        self.pushButton.clicked.connect(self.pushButton_clicked)

        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
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

    def lineEdit_1_double_click(self,event):
        select_file = QtWidgets.QFileDialog.getOpenFileName(self,filter='*.tif')
        print(select_file)
        if select_file[0] != "":
            self.lineEdit_1.setText(select_file[0])
        else:
            self.lineEdit_1.setText(self.lineEdit_1.text())

    def lineEdit_2_double_click(self,event):
        select_file = QtWidgets.QFileDialog.getOpenFileName(self,filter='*.tif')
        print(select_file)
        if select_file[0] != "":
            self.lineEdit_2.setText(select_file[0])
        else:
            self.lineEdit_2.setText(self.lineEdit_2.text())

    def lineEdit_3_double_click(self,event):
        select_file = QtWidgets.QFileDialog.getOpenFileName(self,filter='*.brs')
        print(select_file)
        if select_file[0] != "":
            self.lineEdit_3.setText(select_file[0])
            utc_line, number, p, s = Read_brs.readFile(select_file[0])
            self.label_5.setText("UTC:"+utc_line+" P:"+p+" S:"+s)
            print(utc_line,number,p,s)
        else:
            self.lineEdit_3.setText(self.lineEdit_3.text())


    def lineEdit_4_double_click(self,event):
        select_file = QtWidgets.QFileDialog.getExistingDirectory(self)
        print(select_file)
        if select_file.strip() != "":
            self.lineEdit_4.setText(select_file)
        else:
            self.lineEdit_4.setText(self.lineEdit_4.text())

    def lineEdit_5_double_click(self,event):
        s1=""
        s2=""
        if self.lineEdit_1.text().strip() != "":
            s1 = self.lineEdit_1.text().strip().split("/")[-1].split(".")[0]
        if self.lineEdit_2.text().strip() != "":
            s2 = self.lineEdit_2.text().strip().split("/")[-1].split(".")[0]
        self.lineEdit_5.setText(s1+"_"+s2+"_"+"SSR.tif")

    def pushButton_clicked(self):
        self.target = True
        if self.lineEdit_1.text().strip()=="" or self.lineEdit_2.text().strip()=="" or self.lineEdit_3.text().strip()=="" or \
            self.lineEdit_4.text().strip()=="" or self.lineEdit_5.text().strip()=="" or self.label_5.text().strip()=="":
            self.showDialog_ok("Error","Please check the information completion!")
        if not self.target:#用户确认检查数据的完整性，此时任务执行结束
           return
        print(self.target)
        image1 = self.lineEdit_1.text()
        image2 = self.lineEdit_2.text()
        img1 = cv2.imread(image1, -1)
        row1, col1 = img1.shape
        img2 = cv2.imread(image2,-1)
        row2, col2 = img2.shape
        del(img1)
        del(img2)
        if row1 != row2 or col1 != col2:
            self.showDialog_ok_cancel("Warn","The size of image1 and image2 are different. " + "\n" + "Is it confirmed that the size is the smallest?")
        if not self.target:#如果数据尺寸不同，且用户不同意用最小尺寸，结束任务
            return
        #self.image1_sensor_angel =





    def showDialog_ok(self,title,message):
        self.dialog_1 = QDialog()
        self.dialog_1.setFixedSize(250,100)
        # pannel = QLabel(self.dialog_1)
        # pannel.setText(message)
        # pannel.move(30,30)
        self.dialog_1.setWindowTitle(title)
        #btn = QtWidgets.QPushButton("ok", self.dialog_1)
        # target = btn.clicked.connect(self.btn_ok_1)
        #btn.move(50, 50)
        self.pbar = QtWidgets.QProgressBar(self.dialog_1)
        # 从左上角30-50的界面，显示一个200*25的界面
        self.pbar.setGeometry(15, 10, 200, 25)  # 设置进度条的位置
        # 设置开始按钮
        self.btn2 = QtWidgets.QPushButton('aa', self.dialog_1)
        self.btn2.move(50, 50)  # 按钮移动的位置
        self.btn2.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        # 计数
        self.step = 0
        self.dialog_1.exec_()


        # 点击按钮
        # 信号函数不能加括号

        # 构建一个计时器



        #self.show()
    def doAction(self):
        # 判断是否处于激活状态
        if self.timer.isActive():
            self.timer.stop()
            self.btn2.setText('开始')
        else:
            self.timer.start(100,self)
            self.btn2.setText('停止')

    def timerEvent(self, *args, **kwargs):
        if self.step>=100:
            # 停止进度条
            self.timer.stop()
            self.btn2.setText('完成')
            return
        self.step+=1
        # 把进度条每次充值的值赋给进图条
        self.pbar.setValue(self.step)

    def showDialog_ok_cancel(self,title,message):
        self.dialog_2 = QDialog()
        self.dialog_2.setFixedSize(300,100)
        pannel = QLabel(self.dialog_2)
        pannel.setText(message)
        pannel.move(10,10)
        self.dialog_2.setWindowTitle(title)

        btn_ok = QtWidgets.QPushButton("ok", self.dialog_2)
        btn_ok.move(50, 50)
        target = btn_ok.clicked.connect(self.btn_ok_2)

        btn_cancel = QtWidgets.QPushButton("cancel", self.dialog_2)
        btn_cancel.move(200, 50)
        target = btn_cancel.clicked.connect(self.btn_cancel_2)


        self.dialog_2.exec_()
        return target

    def btn_ok_1(self):
        self.dialog_1.close()
        self.target = False

    def btn_ok_2(self):
        self.dialog_2.close()
        self.target = True

    def btn_cancel_2(self):
        self.dialog_2.close()
        self.target = False




    # def lineEdit_double_click(self,event):
    #     select_file = QtWidgets.QFileDialog.getOpenFileName(self,filter='*.tif')
    #     print(select_file)
    #     if select_file[0] != "":
    #         self.centralwidget.sender().setText(select_file[0])#可以复用
    #     else:
    #         self.centralwidget.sender().setText(self.centralwidget.sender().text())