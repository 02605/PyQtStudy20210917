import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon
import win32api, win32con

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):

        self.setWindowTitle('Main Message')
        self.resize(300, 200)
        self.setWindowIcon(QIcon('233.JPG'))

        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', 'Sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):

        # 获得窗口
        qr = self.frameGeometry()
        # 获取屏幕中心
        cp = QDesktopWidget().availableGeometry().center()
        # 移动
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())