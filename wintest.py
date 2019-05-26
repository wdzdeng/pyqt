"""
    Created by 壮壮 on 2019/4/22 0022
"""
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

__author__ = "wdz"
from SSR import *



class MyMainWindow(QMainWindow, Ui_Inversion_SSR):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())