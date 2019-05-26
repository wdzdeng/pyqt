# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'globalglint.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel
import time
import numpy as np
import sun_angle
from RoughnessToGlint import roughnessToglintByMatrix
from WriteTiff import writeTiff

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 653)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 653))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 653))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(330, 20, 171, 41))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 80, 171, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 130, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(670, 140, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 140, 171, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(740, 150, 171, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 270, 171, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 260, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 340, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(330, 340, 171, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(620, 330, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(740, 340, 171, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 450, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 10, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 80, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(610, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(740, 20, 171, 41))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(610, 80, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(740, 90, 171, 41))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(670, 260, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(740, 270, 171, 41))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(110, 200, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(330, 200, 171, 41))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(530, 200, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(740, 210, 171, 41))
        self.lineEdit_12.setObjectName("lineEdit_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lineEdit_6.mouseDoubleClickEvent = self.lineEdit_6_double_click
        self.lineEdit_7.mouseDoubleClickEvent = self.lineEdit_7_double_click
        self.pushButton.clicked.connect(self.pushButton_clicked)

    def pushButton_clicked(self):
        top_left_lon = float(self.lineEdit_1.text().strip())
        top_left_lat = float(self.lineEdit_8.text().strip())
        bottom_right_lon = float(self.lineEdit_2.text().strip())
        bottom_right_lat = float(self.lineEdit_9.text().strip())
        if top_left_lat <= bottom_right_lat or top_left_lon >= bottom_right_lon:
            self.showDialog_ok("Error",
                               "please make sure top_left_lat>bottom_right_lat" + "\n" + " and top_left_lon<bottom_right_lon",
                               350, 100)
            return
        row = int(self.lineEdit_3.text().strip())
        col = int(self.lineEdit_4.text().strip())
        utc = self.lineEdit_5.text().strip()
        lon_line = self.get_lon_matrix(col, top_left_lon, bottom_right_lon)
        lat_line = self.get_lat_matrix(row, top_left_lat, bottom_right_lat)
        # Sun_zenith, Sun_azimuth
        sun_zenith_matrix = np.zeros((row, col))
        sun_azimuth_matrix = np.zeros((row, col))
        for i in range(row):
            for j in range(col):
                sun_zenith, sun_azimuth = sun_angle.sun_angle(lon_line[j], lat_line[i], utc)
                sun_zenith_matrix[i, j] = sun_zenith
                sun_azimuth_matrix[i, j] = sun_azimuth
        feng = float(self.lineEdit_10.text().strip())
        Satellite_zenith = float(self.lineEdit_11.text().strip())
        Satellite_azimuth = float(self.lineEdit_12.text().strip())

        # roughnessToglintByMatrix(Satellite_zenith,Satellite_azimuth,Sun_zenith,Sun_azimuth,feng)
        glint_matrix = roughnessToglintByMatrix(Satellite_zenith,Satellite_azimuth,sun_zenith_matrix,sun_azimuth_matrix,feng)
        savePath = self.lineEdit_6.text().strip()+"//"+self.lineEdit_7.text().strip()
        writeTiff(glint_matrix,top_left_lon,top_left_lat,self.pixelWidth, self.pixelHeight,savePath)
        #print(max(glint_matrix))

    def get_lon_matrix(self, col, top_left_lon, bottom_right_lon):
        # step = (bottom_right_lon - top_left_lon)/(col-1)
        # lon_maxtrix = np.zeros((row,col))
        # lon_maxtrix[:,0] = top_left_lon
        # for i in range(1,col):
        #     lon_maxtrix[:,i]=lon_maxtrix[0,i-1]+step
        # return lon_maxtrix

        step = (bottom_right_lon - top_left_lon) / (col - 1)
        self.pixelWidth = step
        lon_maxtrix = np.zeros((col))
        lon_maxtrix[0] = top_left_lon
        for i in range(1, col):
            lon_maxtrix[i] = lon_maxtrix[i - 1] + step
        return lon_maxtrix

    def get_lat_matrix(self, row, top_left_lat, bottom_right_lat):
        # step = (bottom_right_lat - top_left_lat)/(row-1)
        # lat_maxtrix = np.zeros((row,col))
        # lat_maxtrix[0,:] = top_left_lat
        # for i in range(1,row):
        #     lat_maxtrix[i,:]=lat_maxtrix[i-1,0]+step
        # return lat_maxtrix
        step = (bottom_right_lat - top_left_lat) / (row - 1)
        self.pixelHeight = step
        lat_maxtrix = np.zeros((row))
        lat_maxtrix[0] = top_left_lat
        for i in range(1, row):
            lat_maxtrix[i] = lat_maxtrix[i - 1] + step
        return lat_maxtrix

    def lineEdit_6_double_click(self, event):
        select_file = QtWidgets.QFileDialog.getExistingDirectory(self)
        select_file = select_file.strip()
        if select_file != "":
            if select_file[-1] == "/":
                self.lineEdit_6.setText(select_file[:-1])
            else:
                self.lineEdit_6.setText(select_file)
        else:
            self.lineEdit_6.setText(self.lineEdit_4.text())

    def lineEdit_7_double_click(self, event):
        filename = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())) + ".tif"
        self.lineEdit_7.setText(filename)

    def showDialog_ok(self, title, message, width, high):
        self.dialog_1 = QDialog()
        self.dialog_1.setFixedSize(width, high)
        pannel = QLabel(self.dialog_1)
        pannel.setText(message)
        pannel.move(30, 20)
        self.dialog_1.setWindowTitle(title)
        btn = QtWidgets.QPushButton("ok", self.dialog_1)
        btn.clicked.connect(self.btn_ok_1)
        btn.move(100, 50)
        self.dialog_1.exec_()

    def btn_ok_1(self):

        self.dialog_1.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Top Left"))
        self.label_2.setText(_translate("MainWindow", "Bottom Right"))
        self.label_3.setText(_translate("MainWindow", "Row"))
        self.label_4.setText(_translate("MainWindow", "Col"))
        self.label_5.setText(_translate("MainWindow", "UTC"))
        self.label_6.setText(_translate("MainWindow", "Save Path"))
        self.label_7.setText(_translate("MainWindow", "File Name"))
        self.pushButton.setText(_translate("MainWindow", "Execute"))
        self.label_8.setText(_translate("MainWindow", "Longitude"))
        self.label_9.setText(_translate("MainWindow", "Longitude"))
        self.label_10.setText(_translate("MainWindow", "Latitude"))
        self.label_11.setText(_translate("MainWindow", "Latitude"))
        self.label_12.setText(_translate("MainWindow", "Wind"))
        self.label_13.setText(_translate("MainWindow", "Satellite Zenith"))
        self.label_14.setText(_translate("MainWindow", "Satellite Azimuth"))

