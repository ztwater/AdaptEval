pytest -v --tb=line
============================= test session starts =============================
[...]
collected 4 items

test_example.py::test_my_fixture_running_success PASSED
test_example.py::test_my_fixture_running_fail FAILED
test_example.py::test_my_fixture_stopped_success PASSED
test_example.py::test_my_fixture_stopped_fail FAILED

================================== FAILURES ===================================
C:\test_example.py:21: assert False
C:\test_example.py:31: assert False
===================== 2 failed, 2 passed in 0.16 seconds ======================
