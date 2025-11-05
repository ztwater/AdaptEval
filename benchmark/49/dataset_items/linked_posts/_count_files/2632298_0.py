def count_em(valid_path):
   x = 0
   for root, dirs, files in os.walk(valid_path):
       for f in files:
            x = x+1
print "There are", x, "files in this directory."
return x
