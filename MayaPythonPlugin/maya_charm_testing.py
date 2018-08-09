# coding:utf-8
# 测试 PyCharm 的 MayaCharm 插件是否安装好 By Jason (184327932@qq.com), 公众号: WendyAndAndy

from maya import cmds
from random import uniform

cmds.file(new=True, f=True)
objs = []
for i in range(80):
    t, s = cmds.polyCube(n = 'box_%s'%i)
    objs.append(t)

    x = uniform(-15, 15)
    y = uniform(-15, 15)
    z = uniform(-15, 15)
    cmds.move(x, y, z, t)

    rx = uniform(0, 360)
    ry = uniform(0, 360)
    rz = uniform(0, 360)
    cmds.rotate(rx, ry, rz, t)

    scale = uniform(0.35, 1.8)
    cmds.scale(scale, scale, scale, t)


cmds.select(objs)