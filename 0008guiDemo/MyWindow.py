# coding:utf-8
# based Maya2017 PySide2
# WeChat: WendyAndAndy (TAsThinking, iJasonLee)

import sys
import guiDemo_ui
from PySide2 import QtGui, QtWidgets, QtCore
# from Qt import QtGui, QtWidgets, QtCore


class MyWindow(QtWidgets.QWidget, guiDemo_ui.Ui_Form):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        if parent:
            self.setWindowFlags(parent.windowFlags())

        self.btnCreate.clicked.connect(self.btnCreate_clicked)
        self.btnRename.clicked.connect(self.btnRename_clicked)

    def btnCreate_clicked(self):
        print('btnCreate_clicked')

    def btnRename_clicked(self):
        print('btnRename_clicked')


def main():
    app = QtWidgets.QApplication(sys.argv)

    global win
    try:
        win.close()
    except:
        pass
    win = MyWindow(None)
    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()