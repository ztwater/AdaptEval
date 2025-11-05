def populateTreeView(control, parent, parentname, counter):
    # list all the children of the parent node
    children = cmds.listRelatives(parent, children=True, path=True) or []

    # loop over the children
    for child in children:
        # childname is the string after the last '|'
        childname = child.rsplit('|')[-1]

        # increment the number of spaces
        counter[childname] += 1
        # make a new string with counter spaces following the name
        childname = '{0} {1}'.format(childname, ' '*counter[childname])

        # create the leaf in the treeView, named childname, parent parentname
        cmds.treeView(control, e=True, addItem=(childname, parentname))

        # call this function again, with child as the parent. recursion!
        populateTreeView(control, child, childname, counter)


# find the selected object
selection = cmds.ls(sl=True)[0]

# create the root node in the treeView
cmds.treeView(control, e=True, addItem=(selection, ''), hideButtons=True)

# enter the recursive function
populateTreeView(control, selection, '', defaultdict(int))
