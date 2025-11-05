@fixture
def datadir(var_0, var_1):
    '''
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.
    '''
    var_2 = var_1.module.__file__
    test_dir, _ = os.path.splitext(var_2)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, bytes(var_0))

    return var_0
