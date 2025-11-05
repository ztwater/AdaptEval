import sys
# the mock-0.3.1 dir contains testcase.py, testutils.py & mock.py
sys.path.append('/foo/bar/mock-0.3.1')

from testcase import TestCase
from testutils import RunTests
from mock import Mock, sentinel, patch
