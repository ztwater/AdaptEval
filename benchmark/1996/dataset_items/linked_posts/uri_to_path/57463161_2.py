import os
import pytest

def validate(file_uri, expected_windows_path, expected_posix_path):
    if expected_windows_path is not None:
        expected_windows_path_object = pathlib.PureWindowsPath(expected_windows_path)
    if expected_posix_path is not None:
        expected_posix_path_object = pathlib.PurePosixPath(expected_posix_path)

    if expected_windows_path is not None:
        if os.name == "nt":
            assert file_uri_to_path(file_uri) == expected_windows_path_object
        assert file_uri_to_path(file_uri, pathlib.PureWindowsPath) == expected_windows_path_object

    if expected_posix_path is not None:
        if os.name != "nt":
            assert file_uri_to_path(file_uri) == expected_posix_path_object
        assert file_uri_to_path(file_uri, pathlib.PurePosixPath) == expected_posix_path_object


def test_some_paths():
    validate(pathlib.PureWindowsPath(r"C:\Windows\System32\Drivers\etc\hosts").as_uri(),
        expected_windows_path=r"C:\Windows\System32\Drivers\etc\hosts",
        expected_posix_path=r"/C:/Windows/System32/Drivers/etc/hosts")

    validate(pathlib.PurePosixPath(r"/C:/Windows/System32/Drivers/etc/hosts").as_uri(),
        expected_windows_path=r"C:\Windows\System32\Drivers\etc\hosts",
        expected_posix_path=r"/C:/Windows/System32/Drivers/etc/hosts")

    validate(pathlib.PureWindowsPath(r"C:\some dir\some file").as_uri(),
        expected_windows_path=r"C:\some dir\some file",
        expected_posix_path=r"/C:/some dir/some file")

    validate(pathlib.PurePosixPath(r"/C:/some dir/some file").as_uri(),
        expected_windows_path=r"C:\some dir\some file",
        expected_posix_path=r"/C:/some dir/some file")

def test_invalid_url():
    with pytest.raises(ValueError) as excinfo:
        validate(r"file://C:/test/doc.txt",
            expected_windows_path=r"test\doc.txt",
            expected_posix_path=r"/test/doc.txt")
        assert "is not absolute" in str(excinfo.value)

def test_escaped():
    validate(r"file:///home/user/some%20file.txt",
        expected_windows_path=None,
        expected_posix_path=r"/home/user/some file.txt")
    validate(r"file:///C:/some%20dir/some%20file.txt",
        expected_windows_path="C:\some dir\some file.txt",
        expected_posix_path=r"/C:/some dir/some file.txt")

def test_no_authority():
    validate(r"file:c:/path/to/file",
        expected_windows_path=r"c:\path\to\file",
        expected_posix_path=None)
    validate(r"file:/path/to/file",
        expected_windows_path=None,
        expected_posix_path=r"/path/to/file")
