import sys
from PyQt5.QtWidgets import QApplication, QWidget
import win32api, win32con

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(550, 150)
    w.move(win32api.GetSystemMetrics(win32con.SM_CXSCREEN)/2.5, win32api.GetSystemMetrics(win32con.SM_CYSCREEN)/2.5)
    w.setWindowTitle("Hello QT")
    w.show()
    sys.exit(app.exec_())