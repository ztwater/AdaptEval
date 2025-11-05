import sys

filepath = 'C:\\path\\to\\your\\file.txt'

try:
    filehandle = open( filepath, 'w' )
except IOError:
    sys.exit( 'Unable to write to file ' + filepath )

filehandle.write("I am writing this text to the file\n")
