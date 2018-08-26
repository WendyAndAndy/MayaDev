# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\git\WendyAndAndy\MayaDev\0008guiDemo\guiDemo.ui'
#
# Created: Mon Aug 27 01:02:05 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 180)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.cbObjType = QtWidgets.QComboBox(Form)
        self.cbObjType.setObjectName("cbObjType")
        self.cbObjType.addItem("")
        self.cbObjType.addItem("")
        self.gridLayout.addWidget(self.cbObjType, 0, 1, 1, 1)
        self.btnCreate = QtWidgets.QPushButton(Form)
        self.btnCreate.setObjectName("btnCreate")
        self.gridLayout.addWidget(self.btnCreate, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.leNewName = QtWidgets.QLineEdit(Form)
        self.leNewName.setObjectName("leNewName")
        self.gridLayout.addWidget(self.leNewName, 1, 1, 1, 1)
        self.btnRename = QtWidgets.QPushButton(Form)
        self.btnRename.setObjectName("btnRename")
        self.gridLayout.addWidget(self.btnRename, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "WendyAndAndy Demo", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "object type:", None, -1))
        self.cbObjType.setItemText(0, QtWidgets.QApplication.translate("Form", "box", None, -1))
        self.cbObjType.setItemText(1, QtWidgets.QApplication.translate("Form", "sphere", None, -1))
        self.btnCreate.setText(QtWidgets.QApplication.translate("Form", "Create", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "new name:", None, -1))
        self.btnRename.setText(QtWidgets.QApplication.translate("Form", "Rename", None, -1))

