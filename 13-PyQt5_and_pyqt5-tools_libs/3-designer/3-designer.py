from MyWindowFile import Ui_MyWindow
import PyQt5
import sys
from PyQt5 import QtWidgets



class ExampleClass(QtWidgets.QMainWindow):
    def __init__(self):
        super(ExampleClass, self).__init__()
        self.ui = Ui_MyWindow()
        self.ui.setupUi(self)
        self.ui.addition_button.clicked.connect(self.compute)
        self.ui.substraction_button.clicked.connect(self.compute)
        self.ui.multiplication_button.clicked.connect(self.compute)
        self.ui.division_button.clicked.connect(self.compute)
    
    def compute(self):
        result = 0
        if self.sender().text() == 'Add':
            result = int(self.ui.lineEdit_1.text()) + int(self.ui.lineEdit_2.text())
        elif self.sender().text() == 'Substract':
            result = int(self.ui.lineEdit_1.text()) - int(self.ui.lineEdit_2.text())
        elif self.sender().text() == 'Multiply':
            result = int(self.ui.lineEdit_1.text()) * int(self.ui.lineEdit_2.text())
        elif self.sender().text() == 'Divide':
            result = int(self.ui.lineEdit_1.text()) / int(self.ui.lineEdit_2.text())
        
        self.ui.label_result.setText("Result is: " + str(result))

app = QtWidgets.QApplication(sys.argv)

ex = ExampleClass()
ex.show()

sys.exit(app.exec_())
