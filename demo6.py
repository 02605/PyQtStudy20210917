import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QDesktopWidget, QLabel,QPushButton,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):

        self.setWindowTitle('Buttons')
        self.resize(500, 300)
        self.setWindowIcon(QIcon('233.JPG'))
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
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