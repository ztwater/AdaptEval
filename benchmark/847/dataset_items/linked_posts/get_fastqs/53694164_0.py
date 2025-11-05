#First, get the files:
import glob
import re
files =glob.glob1(img_folder,'*'+output_image_format)
# if you want sort files according to the digits included in the filename, you can do as following:
files = sorted(files, key=lambda x:float(re.findall("(\d+)",x)[0]))
