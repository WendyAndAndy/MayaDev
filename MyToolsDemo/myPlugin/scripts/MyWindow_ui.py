# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\git\WendyAndAndy\MayaDev\MyToolsDemo\myPlugin\scripts\MyWindow.ui'
#
# Created: Sat Aug 25 01:12:43 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 150)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnCreateSphere = QtWidgets.QPushButton(Form)
        self.btnCreateSphere.setObjectName("btnCreateSphere")
        self.verticalLayout.addWidget(self.btnCreateSphere)
        self.btnCallCppPlugin = QtWidgets.QPushButton(Form)
        self.btnCallCppPlugin.setObjectName("btnCallCppPlugin")
        self.verticalLayout.addWidget(self.btnCallCppPlugin)
        self.btnCallCSPlugin = QtWidgets.QPushButton(Form)
        self.btnCallCSPlugin.setObjectName("btnCallCSPlugin")
        self.verticalLayout.addWidget(self.btnCallCSPlugin)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "WendyAndAndy", None, -1))
        self.btnCreateSphere.setText(QtWidgets.QApplication.translate("Form", "Create Sphere", None, -1))
        self.btnCallCppPlugin.setText(QtWidgets.QApplication.translate("Form", "Call C++ Plugin", None, -1))
        self.btnCallCSPlugin.setText(QtWidgets.QApplication.translate("Form", "Call C# Plugin", None, -1))

