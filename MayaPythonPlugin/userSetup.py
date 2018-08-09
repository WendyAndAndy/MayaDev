# coding:utf-8
# 用于 PyCharm 的 MayaCharm 插件 By Jason (184327932@qq.com), 公众号: WendyAndAndy
# 将这个文件放在：我的文档\maya\版本号\scripts 目录里
from maya import cmds
if not cmds.commandPort(':4434', q=True):
    cmds.commandPort(n=':4434')