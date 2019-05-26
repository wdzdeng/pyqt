"""
    Created by 壮壮 on 2019/3/25 0025
"""
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from firstMainWin import Ui_MainWindow

from firstMainWin import *

__author__ = "wdz"


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())
