pytest -v --tb=line
============================= test session starts =============================
[...]
collected 4 items

test_example.py::test_my_fixture_running_success PASSED
test_example.py::test_my_fixture_running_fail SKIPPED
test_example.py::test_my_fixture_stopped_success PASSED
test_example.py::test_my_fixture_stopped_fail SKIPPED

===================== 2 passed, 2 skipped in 0.10 seconds =====================
