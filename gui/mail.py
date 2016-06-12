# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mail.ui'
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

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(320, 250)
        self.textEdit = QtGui.QTextEdit(dialog)
        self.textEdit.setGeometry(QtCore.QRect(80, 20, 201, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label = QtGui.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 56, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit_2 = QtGui.QTextEdit(dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 70, 201, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label_2 = QtGui.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 56, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 56, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit_3 = QtGui.QTextEdit(dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(80, 130, 201, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.pushButton = QtGui.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 180, 140, 50))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 180, 140, 50))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), dialog.slot1_click)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), dialog.slot3_click)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "메일", None))
        self.label.setText(_translate("dialog", "G mail ID ", None))
        self.label_2.setText(_translate("dialog", "password", None))
        self.label_3.setText(_translate("dialog", "받는 사람", None))
        self.pushButton.setText(_translate("dialog", "보내기", None))
        self.pushButton_3.setText(_translate("dialog", "나가기", None))

