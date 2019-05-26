"""
    Created by 壮壮 on 2018/12/7 0007
"""
__author__ = "wdz"
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QLineEdit, QMessageBox, QDesktopWidget, QTextEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Calculater(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        Font = QFont('SansSerif', 18)
        self.resize(500, 400)
        self.move(100, 100)
        self.setWindowTitle("壮哥的计算器")
        self.setWindowIcon(QIcon('./1.jpg'))
        self.center()
        self.line = QLineEdit(self)
        self.line.resize(480, 80)
        self.line.move(10, 10)
        self.line.setFont(Font)

        self.Text = QTextEdit(self)
        self.Text.resize(480, 280)
        self.Text.move(10, 110)
        self.Text.setFont(Font)
        self.Text.setText(str(0))

        self.line.textChanged.connect(self.calculate)
        self.show()

    def calculate(self):
        s = self.line.text()
        if len(s) == 0:
            self.Text.setText(str(0))
            return False
        s = s.replace('^', '**')  # 使得能够接受^这样的用法
        try:
            ans = eval(s)
        except:
            return False
        else:
            self.Text.setText(str(ans))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Calculater()

    sys.exit(app.exec_())
