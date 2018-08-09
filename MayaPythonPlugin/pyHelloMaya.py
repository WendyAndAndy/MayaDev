# coding:utf-8
# 一个简单的Maya Python插件 By Jason (184327932@qq.com), 公众号: WendyAndAndy

import sys
from maya.api import OpenMaya as om

def maya_useNewAPI():
    pass

__VENDOR = 'kingmax_res@163.com | 184327932@qq.com | iJasonLee@WeChat'
__VERSION= '2018.08.08.01'


class HelloMaya(om.MPxCommand):
    command = 'pyHello'

    def __init__(self):
        super(HelloMaya, self).__init__()

    def doIt(self, args):
        print(u'Hello, Maya. 中文测试：你好，妈呀！')

    @staticmethod
    def creator():
        return HelloMaya()


def initializePlugin(obj):
    plugin = om.MFnPlugin(obj, __VENDOR, __VERSION)
    try:
        plugin.registerCommand(HelloMaya.command, HelloMaya.creator)
    except:
        sys.stderr.write('register pyHello command failed')
        raise


def uninitializePlugin(obj):
    plugin = om.MFnPlugin(obj, __VENDOR, __VERSION)
    try:
        plugin.deregisterCommand(HelloMaya.command)
    except:
        sys.stderr.write('deregister pyHello command failed')
        raise


