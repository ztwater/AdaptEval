# Some extracts from the test suite of the natsort library. Permalink:
# https://github.com/SethMMorton/natsort/blob/e3c32f5638bf3a0e9a23633495269bea0e75d379/tests/test_natsorted.py

sort_data = [
    (  # same as test_natsorted_can_sort_as_unsigned_ints_which_is_default()
        ["a50", "a51.", "a50.31", "a-50", "a50.4", "a5.034e1", "a50.300"],
        ["a5.034e1", "a50", "a50.4", "a50.31", "a50.300", "a51.", "a-50"],
    ),
    (  # same as test_natsorted_numbers_in_ascending_order()
        ["a2", "a5", "a9", "a1", "a4", "a10", "a6"],
        ["a1", "a2", "a4", "a5", "a6", "a9", "a10"],
    ),
    (  # same as test_natsorted_can_sort_as_version_numbers()
        ["1.9.9a", "1.11", "1.9.9b", "1.11.4", "1.10.1"],
        ["1.9.9a", "1.9.9b", "1.10.1", "1.11", "1.11.4"],
    ),
    (  # different from test_natsorted_handles_filesystem_paths()
        [
            "/p/Folder (10)/file.tar.gz",
            "/p/Folder (1)/file (1).tar.gz",
            "/p/Folder/file.x1.9.tar.gz",
            "/p/Folder (1)/file.tar.gz",
            "/p/Folder/file.x1.10.tar.gz",
        ],
        [
            "/p/Folder (1)/file (1).tar.gz",
            "/p/Folder (1)/file.tar.gz",
            "/p/Folder (10)/file.tar.gz",
            "/p/Folder/file.x1.9.tar.gz",
            "/p/Folder/file.x1.10.tar.gz",
        ],
    ),
    (  # same as test_natsorted_path_extensions_heuristic()
        [
            "Try.Me.Bug - 09 - One.Two.Three.[text].mkv",
            "Try.Me.Bug - 07 - One.Two.5.[text].mkv",
            "Try.Me.Bug - 08 - One.Two.Three[text].mkv",
        ],
        [
            "Try.Me.Bug - 07 - One.Two.5.[text].mkv",
            "Try.Me.Bug - 08 - One.Two.Three[text].mkv",
            "Try.Me.Bug - 09 - One.Two.Three.[text].mkv",
        ],
    ),
    (  # same as ns.IGNORECASE for test_natsorted_supports_case_handling()
        ["Apple", "corn", "Corn", "Banana", "apple", "banana"],
        ["Apple", "apple", "Banana", "banana", "corn", "Corn"],
    ),

]

for (given, expected) in sort_data:
    assert sorted(given, key=string_to_pairs) == expected
