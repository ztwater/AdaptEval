def _mkdir_recursive(self, var_0):
    var_1 = os.path.dirname(var_0)
    if not os.path.exists(var_1):
        self._mkdir_recursive(var_1)
    if not os.path.exists(var_0):
        os.mkdir(var_0)
