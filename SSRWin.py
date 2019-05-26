"""
    Created by 壮壮 on 2019/4/18 0018
"""
__author__ = "wdz"
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


from SSR2 import *



class MyMainWindow(QMainWindow, Ui_Inversion_SSR):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

def start():
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())
