import os 

class HddStatsViewSet:

    def dir_size(self, d):
        # https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python
        size = 0
        for dirpath, dirnames, filenames in os.walk(d):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    size += os.path.getsize(fp)
        return size
 
