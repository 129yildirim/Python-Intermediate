# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyWindow(object):
    def setupUi(self, MyWindow):
        MyWindow.setObjectName("MyWindow")
        MyWindow.resize(520, 370)
        self.centralwidget = QtWidgets.QWidget(MyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.division_button = QtWidgets.QPushButton(self.centralwidget)
        self.division_button.setGeometry(QtCore.QRect(370, 230, 93, 28))
        self.division_button.setObjectName("division_button")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(120, 95, 91, 31))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 160, 91, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(190, 100, 113, 22))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 170, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.addition_button = QtWidgets.QPushButton(self.centralwidget)
        self.addition_button.setGeometry(QtCore.QRect(20, 230, 93, 28))
        self.addition_button.setObjectName("addition_button")
        self.substraction_button = QtWidgets.QPushButton(self.centralwidget)
        self.substraction_button.setGeometry(QtCore.QRect(140, 230, 93, 28))
        self.substraction_button.setObjectName("substraction_button")
        self.multiplication_button = QtWidgets.QPushButton(self.centralwidget)
        self.multiplication_button.setGeometry(QtCore.QRect(250, 230, 93, 28))
        self.multiplication_button.setObjectName("multiplication_button")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(170, 280, 141, 31))
        self.label_result.setObjectName("label_result")
        MyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 26))
        self.menubar.setObjectName("menubar")
        MyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MyWindow)
        self.statusbar.setObjectName("statusbar")
        MyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MyWindow)
        QtCore.QMetaObject.connectSlotsByName(MyWindow)

    def retranslateUi(self, MyWindow):
        _translate = QtCore.QCoreApplication.translate
        MyWindow.setWindowTitle(_translate("MyWindow", "MainWindow"))
        self.division_button.setText(_translate("MyWindow", "Divide"))
        self.label_1.setText(_translate("MyWindow", "Num 1:"))
        self.label_2.setText(_translate("MyWindow", "Num 2:"))
        self.addition_button.setText(_translate("MyWindow", "Add"))
        self.substraction_button.setText(_translate("MyWindow", "Substract"))
        self.multiplication_button.setText(_translate("MyWindow", "Multiply"))
        self.label_result.setText(_translate("MyWindow", "Result is: "))