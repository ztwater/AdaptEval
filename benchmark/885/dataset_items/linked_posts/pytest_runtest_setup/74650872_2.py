$ pytest -v test_reports.py --no-header
================= test session starts =================
collected 2 items

test_reports.py::test_skip_if_no_cli_tag SKIPPED [ 50%]
test_reports.py::test_always_run PASSED         [100%]

============ 1 passed, 1 skipped in 0.00s =============

$ MY_SPECIAL_FLAG=1 pytest -v test_reports.py --no-header
================= test session starts =================
collected 2 items

test_reports.py::test_skip_if_no_cli_tag PASSED [ 50%]
test_reports.py::test_always_run PASSED         [100%]

================== 2 passed in 0.00s ==================
