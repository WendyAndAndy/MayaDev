# coding:utf-8
# python maya plugin for MyToolsDemo (mainWindow)

import MyWindow_ui
from maya import cmds
from PySide2 import QtWidgets, QtGui, QtCore
from maya import OpenMayaUI
from shiboken2 import wrapInstance


def getMayaMainWindow():
    mayaMainWindow = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(mayaMainWindow), QtWidgets.QMainWindow)


class Win(QtWidgets.QWidget, MyWindow_ui.Ui_Form):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.setupUi(self)
        if parent:
            self.setWindowFlags(parent.windowFlags())

        self.btnCreateSphere.clicked.connect(self.btnCreateSphere_clicked)
        self.btnCallCppPlugin.clicked.connect(self.btnCallCppPlugin_clicked)
        self.btnCallCSPlugin.clicked.connect(self.btnCallCSPlugin_clicked)

    def btnCreateSphere_clicked(self):
        print('btnCreateSphere_clicked')
        cmds.polySphere()

    def btnCallCppPlugin_clicked(self):
        print('btnCallCppPlugin_clicked')
        try:
            cmds.loadPlugin('HelloMaya')
            cmds.myCmd1()
            cmds.hello()
        except Exception as ex:
            cmds.error(ex.message)

    def btnCallCSPlugin_clicked(self):
        print('btnCallCSPlugin_clicked')
        try:
            cmds.loadPlugin('HiMaya2017')
            cmds.csHi()
        except Exception as ex:
            cmds.error(ex.message)


def main():
    # app = QtWidgets.QApplication(sys.argv)
    global win
    try:
        win.close()
    except:
        pass
    win = Win(getMayaMainWindow())
    win.show()
    # sys.exit(app.exec_())


if __name__ == '__main__':
    main()