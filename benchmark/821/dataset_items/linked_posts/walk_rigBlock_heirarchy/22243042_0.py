from maya import cmds
from collections import defaultdict

window = cmds.window()
layout = cmds.formLayout()

control = cmds.treeView(parent=layout)

cmds.formLayout(layout, e=True, attachForm=[(control,'top', 2),
                                            (control,'left', 2),
                                            (control,'bottom', 2),
                                            (control,'right', 2)])
cmds.showWindow(window)
