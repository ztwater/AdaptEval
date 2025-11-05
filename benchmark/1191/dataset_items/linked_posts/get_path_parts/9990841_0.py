def SplitPath( split_path ):
    pathSplit_lst   = []
    while os.path.basename(split_path):
        pathSplit_lst.append( os.path.basename(split_path) )
        split_path = os.path.dirname(split_path)
    pathSplit_lst.reverse()
    return pathSplit_lst
