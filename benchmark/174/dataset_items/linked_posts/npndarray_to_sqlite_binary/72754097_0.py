import sqlite3, numpy as np, io

def adapt_array(arr):
    out = io.BytesIO()
    np.save(out, arr)
    return sqlite3.Binary(out.getvalue())

sqlite3.register_adapter(np.ndarray, adapt_array)
sqlite3.register_converter("array", lambda x: np.load(io.BytesIO(x)))

x = np.random.rand(100, 100)
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
con.execute("create table test (arr array)")
con.execute("insert into test (arr) values (?)", (x, ))
for r in con.execute("select arr from test"):
    print(r[0])
