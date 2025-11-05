def _mkdir_recursive(self, path):
    sub_path = os.path.dirname(path)
    if not os.path.exists(sub_path):
        self._mkdir_recursive(sub_path)
    if not os.path.exists(path):
        os.mkdir(path)
