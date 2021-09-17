import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import win32api, win32con

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):

        self.setWindowTitle('Hello')
        self.setGeometry(win32api.GetSystemMetrics(win32con.SM_CXSCREEN)/2.5, \
        win32api.GetSystemMetrics(win32con.SM_CYSCREEN)/2.5,
        300, 200)
        self.setWindowIcon(QIcon('233.JPG'))

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())