# import required python modules
# You have to install zipfile package using pip install

import os,zipfile

# Change the directory where you want your new zip file to be

os.chdir('Type your destination')

# Create a new zipfile ( I called it myfile )

zf = zipfile.ZipFile('myfile.zip','w')

# os.walk gives a directory tree. Access the files using a for loop

for dirnames,folders,files in os.walk('Type your directory'):
    zf.write('Type your Directory')
    for file in files:
        zf.write(os.path.join('Type your directory',file))
