sqlite3.register_adapter(np.ndarray, lambda arr: arr.tobytes())
sqlite3.register_converter("array", np.frombuffer)
