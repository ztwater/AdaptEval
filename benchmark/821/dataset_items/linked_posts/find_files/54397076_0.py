import os
onlyfiles = [f for f in os.listdir(file) if len(f) >= 5 and  f[-5:] == ".json" and isfile(join(file, f))]
