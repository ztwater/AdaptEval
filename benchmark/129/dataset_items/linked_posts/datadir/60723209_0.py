import os
import pytest

@pytest.mark.datafiles('/opt/big_files/film1.mp4')
def test_fast_forward(datafiles):
    path = str(datafiles)  # Convert from py.path object to path (str)
    assert len(os.listdir(path)) == 1
    assert os.path.isfile(os.path.join(path, 'film1.mp4'))
    #assert some_operation(os.path.join(path, 'film1.mp4')) == expected_result

    # Using py.path syntax
    assert len(datafiles.listdir()) == 1
    assert (datafiles / 'film1.mp4').check(file=1)
