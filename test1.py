"""
    Created by 壮壮 on 2018/12/7 0007
"""
from PyQt5.QtCore import QCoreApplication

import pyCompute

__author__ = "wdz"
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.resize(500, 150)
        self.move(100, 1000)
        self.setWindowIcon(QIcon('./Title.ico'))
        self.setWindowTitle("Hello world")

        self.setToolTip("<b>this is widget</b>")

        btn = QPushButton("quit Button", self)  # self类似于C++ this指针
        btn.setToolTip("This is a button will quit itself")
        btn.clicked.connect(pyCompute.count)
        btn.resize(btn.sizeHint())
        btn.move(0, 0)
        self.center()

        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())

