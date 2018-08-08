from maya import cmds
if not cmds.commandPort(':4434', q=True):
    cmds.commandPort(n=':4434')