import os
import pytest
import shutil


@pytest.fixture
def datadir(tmppath, request):
    '''
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.

    Taken from stackoverflow
    https://stackoverflow.com/questions/29627341/pytest-where-to-store-expected-data
    (May 6th 2021)
    '''
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        shutil.copytree(test_dir, str(tmppath))

    return tmppath
