"""
    Created by 壮壮 on 2019/4/18 0018
"""
__author__ = "wdz"
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


from Distance import *



class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())

