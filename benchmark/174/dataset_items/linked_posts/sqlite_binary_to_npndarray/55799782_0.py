import sqlite3
import numpy as np

sqlite3.register_adapter(np.array, lambda arr: arr.tobytes())    
sqlite3.register_converter("array", np.frombuffer)
