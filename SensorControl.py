# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SensorControl.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QDialog
import numpy as np
from SensorControlPSO import dealPSO


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 716)
        MainWindow.setMinimumSize(QtCore.QSize(836, 716))
        MainWindow.setMaximumSize(QtCore.QSize(836, 716))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(720, 590, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_39.setGeometry(QtCore.QRect(230, 130, 101, 41))
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_40.setGeometry(QtCore.QRect(230, 240, 101, 41))
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_41.setGeometry(QtCore.QRect(710, 60, 101, 41))
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(60, 60, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_42.setGeometry(QtCore.QRect(350, 240, 101, 41))
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_43.setGeometry(QtCore.QRect(350, 60, 101, 41))
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(40, 430, 433, 98))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_7 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_3.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_3.addWidget(self.checkBox_8)
        self.checkBox_6 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_3.addWidget(self.checkBox_6)
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(60, 190, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(450, 420, 251, 231))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(250, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(480, 240, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(470, 60, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_44.setGeometry(QtCore.QRect(350, 190, 101, 41))
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_45.setGeometry(QtCore.QRect(710, 290, 101, 41))
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_46.setGeometry(QtCore.QRect(710, 240, 101, 41))
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(470, 290, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_47.setGeometry(QtCore.QRect(710, 350, 101, 41))
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.lineEdit_48 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_48.setGeometry(QtCore.QRect(350, 350, 101, 41))
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.lineEdit_49 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_49.setGeometry(QtCore.QRect(710, 120, 101, 41))
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.lineEdit_50 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_50.setGeometry(QtCore.QRect(350, 130, 101, 41))
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(60, 240, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.lineEdit_51 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_51.setGeometry(QtCore.QRect(230, 290, 101, 41))
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.lineEdit_52 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_52.setGeometry(QtCore.QRect(710, 180, 101, 41))
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.lineEdit_53 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_53.setGeometry(QtCore.QRect(230, 350, 101, 41))
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.lineEdit_54 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_54.setGeometry(QtCore.QRect(350, 290, 101, 41))
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(370, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.lineEdit_55 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_55.setGeometry(QtCore.QRect(230, 60, 101, 41))
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(470, 350, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(480, 180, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.lineEdit_56 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_56.setGeometry(QtCore.QRect(230, 190, 101, 41))
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setGeometry(QtCore.QRect(60, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setGeometry(QtCore.QRect(60, 350, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setGeometry(QtCore.QRect(60, 290, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        self.label_45.setGeometry(QtCore.QRect(470, 120, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        self.label_46.setGeometry(QtCore.QRect(50, 550, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.lineEdit_57 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_57.setGeometry(QtCore.QRect(120, 550, 101, 41))
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setGeometry(QtCore.QRect(240, 550, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.lineEdit_58 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_58.setGeometry(QtCore.QRect(330, 550, 101, 41))
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        self.label_48.setGeometry(QtCore.QRect(40, 620, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.lineEdit_59 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_59.setGeometry(QtCore.QRect(330, 610, 101, 41))
        self.lineEdit_59.setObjectName("lineEdit_59")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.checkBox_7.toggled.connect(self.checkBox_7_change)
        self.checkBox_8.toggled.connect(self.checkBox_8_change)
        self.checkBox_6.toggled.connect(self.checkBox_6_change)
        self.pushButton_3.clicked.connect(self.pushButton_3_clicked)

    def pushButton_3_clicked(self):
        sensor1_p_min = float(self.lineEdit_55.text().strip())
        sensor1_p_max = float(self.lineEdit_43.text().strip())

        sensor1_s_min = float(self.lineEdit_39.text().strip())
        sensor1_s_max = float(self.lineEdit_50.text().strip())

        sensor1_v_min = float(self.lineEdit_56.text().strip())
        sensor1_v_max = float(self.lineEdit_44.text().strip())

        sensor2_p_min = float(self.lineEdit_40.text().strip())
        sensor2_p_max = float(self.lineEdit_42.text().strip())

        sensor2_s_min = float(self.lineEdit_51.text().strip())
        sensor2_s_max = float(self.lineEdit_54.text().strip())

        sensor2_v_min = float(self.lineEdit_53.text().strip())
        sensor2_v_max = float(self.lineEdit_48.text().strip())

        opt_sen1_z = float(self.lineEdit_41.text().strip())
        opt_sen1_a = float(self.lineEdit_49.text().strip())
        opt_sen2_z = float(self.lineEdit_52.text().strip())
        opt_sen2_a = float(self.lineEdit_46.text().strip())

        sen1_altitude = float(self.lineEdit_45.text().strip())
        sen2_altitude = float(self.lineEdit_47.text().strip())

        location = [[sensor1_p_min, sensor1_p_max], [sensor1_s_min, sensor1_s_max], [sensor1_v_min, sensor1_v_max], \
                    [sensor2_p_min, sensor2_p_max], [sensor2_s_min, sensor2_s_max], [sensor2_v_min, sensor2_v_max]]

        optimal = np.array([opt_sen1_z, opt_sen1_a, opt_sen2_z, opt_sen2_a])
        p_target = 0
        s_target = 0
        v_target = 0
        if self.checkBox_7.isChecked():
            p_target = 1
        if self.checkBox_8.isChecked():
            s_target = 1
        if self.checkBox_6.isChecked():
            v_target = 1
        target = 0
        if p_target == 1 and s_target == 0 and v_target == 0:
            target = 1
        if p_target == 0 and s_target == 1 and v_target == 0:
            target = 2
        if p_target == 0 and s_target == 0 and v_target == 1:
            target = 3
        if p_target == 1 and s_target == 1 and v_target == 0:
            target = 4
        if p_target == 1 and s_target == 0 and v_target == 1:
            target = 5
        if p_target == 0 and s_target == 1 and v_target == 1:
            target = 6

        error_threshold = 2147483647
        if self.lineEdit_59.text().strip() != "":
            error_threshold = float(self.lineEdit_59.text().strip())
        count = 1
        point = int(self.lineEdit_57.text().strip())
        update = int(self.lineEdit_58.text().strip())
        # def dealPSO(birdNum,update,solutionSpace,h1,h2,optimal,target):
        while (count < 11):
            best_position, best_fit, best_result = dealPSO(point, update, location, sen1_altitude, sen2_altitude,
                                                           optimal, target)
            if best_fit <= error_threshold:
                break
            count += 1
        if count == 11:
            self.showDialog_ok("Error", "执行了十次运算，并未找到符合要求的组合！", 285, 100)
            return
        self.textBrowser_3.setText(
            "Sensor1 P = %f(°) \nSensor1 S = %f(°)\nSensor1 V = %f(°)\nSensor2 P = %f(°)\nSensor2 S = %f(°)\nSensor2 V = %f(°)\n可以得到的成像角度组合如下：\nSensor1 Zenith = %f(°)\nSensor1 Azimuth = %f(°)\nSensor2 Zenith = %f(°)\nSensor2 Azimuth = %f(°) " % ( \
                best_position[0], best_position[1], best_position[2], best_position[3], best_position[4],
                best_position[5], best_result[0], best_result[1], best_result[2], best_result[3]))

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

    def checkBox_7_change(self):
        if self.checkBox_7.isChecked():
            self.lineEdit_40.setText("0")
            self.lineEdit_40.setEnabled(False)
            self.lineEdit_42.setText("0")
            self.lineEdit_42.setEnabled(False)
            if self.checkBox_8.isChecked() and self.checkBox_6.isChecked():
                self.checkBox_8.setChecked(False)

        else:
            self.lineEdit_40.setText("")
            self.lineEdit_40.setEnabled(True)
            self.lineEdit_42.setText("")
            self.lineEdit_42.setEnabled(True)

    def checkBox_8_change(self):
        if self.checkBox_8.isChecked():
            self.lineEdit_51.setText("0")
            self.lineEdit_51.setEnabled(False)
            self.lineEdit_54.setText("0")
            self.lineEdit_54.setEnabled(False)
            if self.checkBox_7.isChecked() and self.checkBox_6.isChecked():
                self.checkBox_7.setChecked(False)

        else:
            self.lineEdit_51.setText("")
            self.lineEdit_51.setEnabled(True)
            self.lineEdit_54.setText("")
            self.lineEdit_54.setEnabled(True)

    def checkBox_6_change(self):
        if self.checkBox_6.isChecked():
            self.lineEdit_53.setText("0")
            self.lineEdit_53.setEnabled(False)
            self.lineEdit_48.setText("0")
            self.lineEdit_48.setEnabled(False)
            if self.checkBox_8.isChecked() and self.checkBox_7.isChecked():
                self.checkBox_7.setChecked(False)

        else:
            self.lineEdit_53.setText("")
            self.lineEdit_53.setEnabled(True)
            self.lineEdit_48.setText("")
            self.lineEdit_48.setEnabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Execute"))
        #self.lineEdit_39.setText(_translate("MainWindow", "0"))
        #self.lineEdit_40.setText(_translate("MainWindow", "-89"))
        #self.lineEdit_41.setText(_translate("MainWindow", "10"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p>Sensor1 P(°)</p></body></html>"))
        #self.lineEdit_42.setText(_translate("MainWindow", "89"))
        #self.lineEdit_43.setText(_translate("MainWindow", "89"))
        self.checkBox_7.setText(_translate("MainWindow", "Sensor1 P = Sensor2 P"))
        self.checkBox_8.setText(_translate("MainWindow", "Sensor1 S = Sensor2 S"))
        self.checkBox_6.setText(_translate("MainWindow", "Sensor1 V = Sensor2 V"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p>Sensor1 V(°)</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Min"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p>Optimal Sen2 A(°)</p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p>Optimal Sen1 Z(°)</p></body></html>"))
        #self.lineEdit_44.setText(_translate("MainWindow", "89"))
       # self.lineEdit_45.setText(_translate("MainWindow", "120"))
        #self.lineEdit_46.setText(_translate("MainWindow", "120"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p>Sensor1 Altitude(m)</p></body></html>"))
        # self.lineEdit_47.setText(_translate("MainWindow", "120"))
        # self.lineEdit_48.setText(_translate("MainWindow", "89"))
        # self.lineEdit_49.setText(_translate("MainWindow", "90"))
        # self.lineEdit_50.setText(_translate("MainWindow", "360"))
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p>Sensor2 P(°)</p></body></html>"))
        # self.lineEdit_51.setText(_translate("MainWindow", "0"))
        # self.lineEdit_52.setText(_translate("MainWindow", "20"))
        # self.lineEdit_53.setText(_translate("MainWindow", "-89"))
        # self.lineEdit_54.setText(_translate("MainWindow", "360"))
        self.label_39.setText(_translate("MainWindow", "Max"))
        #self.lineEdit_55.setText(_translate("MainWindow", "-89"))
        self.label_40.setText(_translate("MainWindow", "<html><head/><body><p>Sensor2 Altitude(m)</p></body></html>"))
        self.label_41.setText(_translate("MainWindow", "<html><head/><body><p>Optimal Sen2 Z(°)</p></body></html>"))
        #self.lineEdit_56.setText(_translate("MainWindow", "-89"))
        self.label_42.setText(_translate("MainWindow", "<html><head/><body><p>Sensor1 S(°)</p></body></html>"))
        self.label_43.setText(_translate("MainWindow", "<html><head/><body><p>Sensor2 V(°)</p></body></html>"))
        self.label_44.setText(_translate("MainWindow", "<html><head/><body><p>Sensor2 S(°)</p></body></html>"))
        self.label_45.setText(_translate("MainWindow", "<html><head/><body><p>Optimal Sen1 A(°)</p></body></html>"))
        self.label_46.setText(_translate("MainWindow", "<html><head/><body><p>Point</p></body></html>"))
        self.lineEdit_57.setText(_translate("MainWindow", "10000"))
        self.label_47.setText(_translate("MainWindow", "<html><head/><body><p>Update</p></body></html>"))
        self.lineEdit_58.setText(_translate("MainWindow", "10"))
        self.label_48.setText(_translate("MainWindow", "<html><head/><body><p>Error Threadshold(°)</p></body></html>"))

