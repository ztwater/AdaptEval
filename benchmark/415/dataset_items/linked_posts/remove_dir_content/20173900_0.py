import os

# Python 2.7
map( os.unlink, (os.path.join( mydir,f) for f in os.listdir(mydir)) )

# Python 3+
list( map( os.unlink, (os.path.join( mydir,f) for f in os.listdir(mydir)) ) )
