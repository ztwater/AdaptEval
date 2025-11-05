def _dir_list(self, dir_name, whitelist):
    outputList = []
    for root, dirs, files in os.walk(dir_name):
        if root == dir_name: #This only meet parent folder
            for f in files:
                if os.path.splitext(f)[1] in whitelist:
                    outputList.append(os.path.join(root, f))
                else:
                    self._email_to_("ignore")
    return outputList
