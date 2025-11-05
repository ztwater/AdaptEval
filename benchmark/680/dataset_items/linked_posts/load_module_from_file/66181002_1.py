Y = LOAD ("../Z.py")
A = LOAD ("./A.py")
D = LOAD ("./C/D.py")
A_ = LOAD ("/IMPORTS/A.py")

Y.DEF ();
A.DEF ();
D.DEF ();
A_.DEF ();
