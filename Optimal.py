# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Optimal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel
from sun_angle import sun_angle
from PSO import dealPSO
import Compare2
import sys

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
        self.checkBox_1.setObjectName("checkBox_1")
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
        self.label_11.setGeometry(QtCore.QRect(570, 200, 211, 41))
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
        self.label_14.setGeometry(QtCore.QRect(70, 530, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(140, 530, 341, 41))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(110, 420, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(190, 420, 101, 41))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(300, 420, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(380, 420, 101, 41))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(490, 330, 401, 241))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(910, 510, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(120, 470, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(190, 470, 101, 41))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(330, 470, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setGeometry(QtCore.QRect(380, 470, 101, 41))
        self.lineEdit_19.setText("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(560, 260, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_20.setGeometry(QtCore.QRect(790, 260, 101, 41))
        self.lineEdit_20.setObjectName("lineEdit_20")
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
        sensor1_zenith_max = float(self.lineEdit_2.text().strip()) if float(self.lineEdit_2.text().strip()) < 90 else 89
        sensor1_Azimuth_min = float(self.lineEdit_3.text().strip())
        sensor1_Azimuth_max = float(self.lineEdit_4.text().strip())

        sensor2_zenith_min = float(self.lineEdit_5.text().strip())
        sensor2_zenith_max = float(self.lineEdit_6.text().strip()) if float(self.lineEdit_6.text().strip()) < 90 else 89
        sensor2_Azimuth_min = float(self.lineEdit_7.text().strip())
        sensor2_Azimuth_max = float(self.lineEdit_8.text().strip())

        if sensor1_zenith_max < sensor1_zenith_min or sensor1_Azimuth_max < sensor1_Azimuth_min or sensor2_zenith_max < sensor2_zenith_min or sensor2_Azimuth_max < sensor2_Azimuth_min:
            self.showDialog_ok("Error", "Please confirm Max >= Min !", 200, 100)
            return
        location = [[sensor1_zenith_min, sensor1_zenith_max], [sensor1_Azimuth_min, sensor1_Azimuth_max],
                    [sensor2_zenith_min, sensor2_zenith_max], [sensor2_Azimuth_min, sensor2_Azimuth_max]]
        point = int(self.lineEdit_16.text().strip())
        update = int(self.lineEdit_17.text().strip())
        sensor1_multiply_error = float(self.lineEdit_9.text().strip())
        sensor2_multiply_error = float(self.lineEdit_10.text().strip())
        sensor_add_error = float(self.lineEdit_11.text().strip())
        feng = float(self.lineEdit_14.text().strip())
        if self.lineEdit_12.text().strip() != "" and self.lineEdit_13.text().strip() != "":
            sun_zenith = float(self.lineEdit_12.text())
            sun_azimuth = float(self.lineEdit_13.text())
        else:
            utc = self.lineEdit_15.text()
            lon = float(self.lineEdit_18.text().strip())
            lat = float(self.lineEdit_19.text().strip())
            sun_zenith, sun_azimuth = sun_angle(lon, lat, utc)
        # dealPSO(birdNum,update,solutionSpace,sun_zenith,sun_azimuth,feng,N_deviation,B_deviation,add_deviation,target):
        target = 0
        if self.checkBox_1.isChecked():
            target = 1
        if self.checkBox_2.isChecked():
            target = 2
        # compare3(N_zenith, N_azimuth, B_zenith, B_azimuth, Sun_zenith, Sun_azimuth, feng, N_deviation, B_deviation,add_deviation)
        error_threshold = 2147483647
        if self.lineEdit_20.text().strip() != "":
            error_threshold = float(self.lineEdit_20.text().strip())
        count = 1
        while (count<11):
            optimal_angele, error = dealPSO(point, update, location, sun_zenith, sun_azimuth, feng,
                                            sensor1_multiply_error,
                                            sensor2_multiply_error, sensor_add_error, target)
            error_max,error_mean = Compare2.compare3(optimal_angele[0],optimal_angele[1],optimal_angele[2],optimal_angele[3],sun_zenith,sun_azimuth, feng,sensor1_multiply_error,sensor2_multiply_error, sensor_add_error)
            if error_max <= error_threshold:
                break
            count +=1
        if count == 11:
            self.showDialog_ok("Error","执行了十次运算，并未找到符合要求的组合！",285,100)
            return



        self.textBrowser.setText(
            "Sensor1 Zenith = %f(°) \nSensor1 Azimuth = %f(°)\nSensor2 Zenith = %f(°)\nSensor2 Azimuth = %f(°) " % (optimal_angele[0], optimal_angele[1], optimal_angele[2], optimal_angele[3])+"\nError = %f()"%(error)+"(%)"+"\nAverage Error = %f"%(error_mean)+"(%)"+"\n Max Error = %f"%(error_max) + "(%)")

        # compare2(N_zenith, N_azimuth, B_zenith, B_azimuth, Sun_zenith, Sun_azimuth, feng, N_deviation, B_deviation,
        #          add_deviation)

        # self.textBrowser.setText(self.textBrowser.text()+"\nerror=%f"%(Compare2.compare2(optimal_angele[0],optimal_angele[1],optimal_angele[2],optimal_angele[3],sun_zenith,sun_azimuth,feng,sensor1_multiply_error,sensor2_multiply_error,sensor_add_error)))

    def showDialog_ok(self, title, message, width, high):
        self.dialog_1 = QDialog()
        self.dialog_1.setFixedSize(width, high)
        pannel = QLabel(self.dialog_1)
        pannel.setText(message)
        pannel.move(10, 20)
        self.dialog_1.setWindowTitle(title)
        btn = QtWidgets.QPushButton("ok", self.dialog_1)
        btn.clicked.connect(self.btn_ok_1)
        btn.move(75, 50)
        self.dialog_1.exec_()

    def btn_ok_1(self):
        self.dialog_1.close()

    def checkBox_1_change(self):
        if self.checkBox_1.isChecked():
            self.lineEdit_5.setText("0")
            self.lineEdit_5.setEnabled(False)
            self.lineEdit_6.setText("0")
            self.lineEdit_6.setEnabled(False)
            if self.checkBox_2.isChecked():
                self.checkBox_2.setChecked(False)

        else:
            self.lineEdit_5.setText("")
            self.lineEdit_5.setEnabled(True)
            self.lineEdit_6.setText("")
            self.lineEdit_6.setEnabled(True)

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
        self.lineEdit_17.setText(_translate("MainWindow", "10"))
        self.pushButton.setText(_translate("MainWindow", "Execute"))
        self.label_17.setText(_translate("MainWindow", "Lon"))
        self.label_18.setText(_translate("MainWindow", "Lat"))
        self.label_19.setText(_translate("MainWindow", "Error Threshold(%)"))
        #self.lineEdit_20.setText(_translate("MainWindow", "10"))
        # self.lineEdit_1.setText(_translate("MainWindow", "0"))
        # self.lineEdit_2.setText(_translate("MainWindow", "30"))
        # self.lineEdit_3.setText(_translate("MainWindow", "0"))
        # self.lineEdit_4.setText(_translate("MainWindow", "360"))
        # self.lineEdit_5.setText(_translate("MainWindow", "0"))
        # self.lineEdit_6.setText(_translate("MainWindow", "30"))
        # self.lineEdit_7.setText(_translate("MainWindow", "0"))
        # self.lineEdit_8.setText(_translate("MainWindow", "360"))
        # self.lineEdit_9.setText(_translate("MainWindow", "4"))
        # self.lineEdit_10.setText(_translate("MainWindow", "7"))
        # self.lineEdit_11.setText(_translate("MainWindow", "0.0005"))
        # self.lineEdit_12.setText(_translate("MainWindow", "20"))
        # self.lineEdit_13.setText(_translate("MainWindow", "90"))
        # self.lineEdit_14.setText(_translate("MainWindow", "5"))





