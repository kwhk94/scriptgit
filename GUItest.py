import sys
from PyQt4 import QtCore, QtGui

from hosdata import *

class MyForm(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def slot1_click(self):
         self.ui.textEdit.append("test")
         return

app = QtGui.QApplication(sys.argv)
myapp = MyForm()
myapp.show()

app.exec_()