diff = difflib.unified_diff(old_file, new_file, lineterm='')
    lines = list(diff)[2:]
    # linesT = list(diff)[0:3]
    print (lines[0])
    added = [lineA for lineA in lines if lineA[0] == '+']


    with open("output.txt", "w") as fh1:
     for line in added:
       fh1.write(line)
    print '+',added
    removed = [lineB for lineB in lines if lineB[0] == '-']
    with open("output.txt", "a") as fh1:
     for line in removed:
       fh1.write(line)
    print '-',removed 
