# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(453, 674)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(190, 30, 141, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 70, 141, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.lineEdit= QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 110, 141, 31))
        self.lineEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 160, 291, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 590, 241, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 220, 431, 361))
        self.tableWidget.setObjectName(_fromUtf8("listWidget"))
        self.tableWidget.setColumnCount(5)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("28 Days Later"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("28 Days Later"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("28 Days Later"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 423, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), mainWindow.access)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), mainWindow.back)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "검색", None))
        self.comboBox.setItemText(0, _translate("mainWindow", "서울", None))
        self.comboBox.setItemText(1, _translate("mainWindow", "부산", None))
        self.comboBox.setItemText(2, _translate("mainWindow", "인천", None))
        self.comboBox.setItemText(3, _translate("mainWindow", "경기", None))
        self.comboBox.setItemText(4, _translate("mainWindow", "강원", None))
        self.comboBox.setItemText(5, _translate("mainWindow", "전북", None))
        self.comboBox.setItemText(6, _translate("mainWindow", "전남", None))
        self.comboBox.setItemText(7, _translate("mainWindow", "광주", None))
        self.comboBox.setItemText(8, _translate("mainWindow", "충북", None))
        self.comboBox.setItemText(9, _translate("mainWindow", "충남", None))
        self.comboBox.setItemText(10, _translate("mainWindow", "울산", None))
        self.comboBox.setItemText(11, _translate("mainWindow", "대전", None))
        self.comboBox.setItemText(12, _translate("mainWindow", "경북", None))
        self.comboBox.setItemText(13, _translate("mainWindow", "경남", None))
        self.comboBox.setItemText(14, _translate("mainWindow", "대구", None))
        self.comboBox.setItemText(15, _translate("mainWindow", "제주", None))
        self.comboBox.setItemText(16, _translate("mainWindow", "세종시", None))
        self.pushButton.setText(_translate("mainWindow", "확인", None))
        self.pushButton_2.setText(_translate("mainWindow", "저장 / 돌아가기", None))
        self.label.setText(_translate("mainWindow", "시     도 ", None))
        self.label_2.setText(_translate("mainWindow", "군     구", None))
        self.label_3.setText(_translate("mainWindow", "병원이름", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "병원이름", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "주소", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "홈페이지", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "tel.no", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "종별", None))

