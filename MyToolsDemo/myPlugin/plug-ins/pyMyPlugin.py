# coding:utf-8
# python maya plugin for MyToolsDemo

import sys
from maya import cmds
from maya.api import OpenMaya as om


def maya_useNewAPI():
    pass


kPluginCmdName = 'MyDemo'
kPluginVendor = 'kingmax_res@163.com | 184327932@qq.com | iJasonLee@WeChat'
kPluginVersion = '2018.08.25.01'


# Menu and Shelf
# ----------------------------------------------------------------------
def removeMenu(menuName=kPluginCmdName):
    """remove menu when plugin unload"""
    if cmds.menu(menuName, q=True, exists=True):
        cmds.deleteUI(menuName, menu=True)


def makeMenu(menuName=kPluginCmdName):
    """make menu when plugin load"""
    removeMenu(menuName)
    topMenu = cmds.menu(menuName, label=menuName, parent=u'MayaWindow', tearOff=True)
    cmds.menuItem(label=kPluginCmdName, parent=topMenu, command=kPluginCmdName, sourceType='mel')


# Plugin class
# ----------------------------------------------------------------------
class MyDemo(om.MPxCommand):
    def __init__(self):
        super(MyDemo, self).__init__()

    def doIt(self, args):
        print('starting %s'%kPluginCmdName)
        try:
            import MyWindow
            reload(MyWindow)
            MyWindow.main()
        except Exception as ex:
            cmds.error(ex.message())

    @staticmethod
    def creator():
        return MyDemo()


# Initialize
# ----------------------------------------------------------------------
def initializePlugin(mobject):
    """Initialize the plug-in and add menu"""
    errMsg = u'Failed to register command: %s\n' % kPluginCmdName
    plugin = om.MFnPlugin(mobject, kPluginVendor, kPluginVersion)
    try:
        plugin.registerCommand(kPluginCmdName, MyDemo.creator)
        makeMenu(menuName=kPluginCmdName)
        # makeShelf(shelfName=kPluginCmdName)
    except:
        sys.stderr.write(errMsg)
        raise

# Uninitialize
# ----------------------------------------------------------------------
def uninitializePlugin(mobject):
    """Uninitialize the plug-in and delete menu"""
    plugin = om.MFnPlugin(mobject)
    try:
        plugin.deregisterCommand(kPluginCmdName)
        removeMenu(menuName=kPluginCmdName)
        # removeShelf(shelfName=kPluginCmdName)
    except:
        sys.stderr.write('Failed to unregister command: %s\n' % kPluginCmdName)
        raise