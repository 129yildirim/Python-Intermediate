import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    
    win = QMainWindow()

    win.show()

    win.setWindowTitle('My Title')
    win.setGeometry(300, 300, 640, 480)
    win.setWindowIcon(QIcon('icon.jpg'))
    win.setToolTip('My Tool Tip')
    

    sys.exit(app.exec_())

window()