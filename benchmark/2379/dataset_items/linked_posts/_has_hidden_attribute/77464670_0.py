import os, sys
from stat import *

def isHidden(path):
    st = os.lstat(path)
    return st.st_flags & UF_HIDDEN
