import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QToolTip, QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    
    

    win.setGeometry(300, 300, 640, 480)
    win.setWindowTitle('Title')
    win.setWindowIcon(QIcon('icon.jpg'))

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Your name: ')
    lbl_name.move(60, 50)
    

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText('Your surname: ')
    lbl_surname.move(60, 100)
    

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150, 50)
    

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150, 100)

    def save_clicked(self):
        print("Clicked. \nName is:", txt_name.text(), "\nSurname is:", txt_surname.text())


    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText('Save')
    btn_save.move(150, 150)

    btn_save.clicked.connect(save_clicked)

    win.show()
    sys.exit(app.exec_())



window()