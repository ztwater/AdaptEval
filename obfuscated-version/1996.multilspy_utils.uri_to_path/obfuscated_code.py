def uri_to_path(var_0):
    var_1 = urlparse(var_0)
    var_2 = "{0}{0}{mnt}{0}".format(os.path.sep, mnt=var_1.netloc)
    return os.path.normpath(
        os.path.join(var_2, url2pathname(unquote(var_1.path)))
    )
