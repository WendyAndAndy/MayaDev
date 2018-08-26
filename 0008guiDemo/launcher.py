# coding:utf-8
# GUI testing for Maya2017, Max2019, Houdini14.0.598
# WeChat: WendyAndAndy (TAsThinking, iJasonLee)

import lib
from MyWindow import MyWindow


def main():
    parent = None

    try:
        import MaxPlus
        parent = lib.getMaxMainWindow()
    except ImportError:
        try:
            import hou
            parent = lib.getHoudiniMainWindow()
        except ImportError:
            try:
                from maya import cmds
                parent = lib.getMayaMainWindow()
            except ImportError:
                pass

    global win
    try:
        win.close()
    except:
        pass
    win = MyWindow(parent)
    win.show()


if __name__ == '__main__':
    main()

