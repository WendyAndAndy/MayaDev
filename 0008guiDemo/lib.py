# coding:utf-8
# get App MainWindow for Max2019, Maya2017, Houdini14.0.598
# WeChat: WendyAndAndy (TAsThinking, iJasonLee)


def getMaxMainWindow():
    import MaxPlus
    return MaxPlus.GetQMaxMainWindow()


def getMayaMainWindow():
    from PySide2 import QtWidgets
    from maya import OpenMayaUI
    from shiboken2 import wrapInstance
    mayaMainWindow = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(mayaMainWindow), QtWidgets.QMainWindow)


def getHoudiniMainWindow():
    from PySide import QtGui
    app = QtGui.QApplication.instance()
    if app:
        parent = app.topLevelAt(QtGui.QCursor().pos())
        if parent:
            return parent
        else:
            # root = app.desktop()
            ws = [w for w in app.topLevelWidgets() if w.windowTitle().count('Houdini') and w.windowType().name == 'Window']
            if ws:
                return ws[0]