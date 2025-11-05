import os

def isWritable(directory):
    try:
        tmp_prefix = "write_tester";
        count = 0
        filename = os.path.join(directory, tmp_prefix)
        while(os.path.exists(filename)):
            filename = "{}.{}".format(os.path.join(directory, tmp_prefix),count)
            count = count + 1
        f = open(filename,"w")
        f.close()
        os.remove(filename)
        return True
    except Exception as e:
        #print "{}".format(e)
        return False

directory = "c:\\"
if (isWritable(directory)):
    print "directory is writable"
else:
    print "directory is not writable"
