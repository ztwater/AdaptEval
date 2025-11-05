import inspect
import platform
import re
import unittest
import socket
from ctx_utils import find_free_port

class TestFindFreePort(unittest.TestCase):
    def test_port_is_free(self):
        # This test checks if the returned port is indeed free
        port = find_free_port()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # This error Code 101 (Linux) / 10061 (Windows), (ECONNREFUSED) indicates that
            # the target port is not currently listening for connections.
            if platform.system() == 'Linux':
                self.assertEqual(s.connect_ex(('localhost', int(port))), 111, "The port should be free (ECONNREFUSED error expected)")
            elif platform.system() == 'Windows':
                self.assertEqual(s.connect_ex(('localhost', int(port))), 10061, "The port should be free (ECONNREFUSED error expected)")

    def test_port_is_string(self):
        # This test checks if the returned port is a string
        port = find_free_port()
        self.assertIsInstance(port, str, "The returned port should be a string")

    def test_port_is_valid(self):
        # This test checks if the returned port is a valid port number
        port = find_free_port()
        self.assertTrue(0 < int(port) < 65536, "The port number should be within the valid range")

    def test_add_imports(self):
        source = inspect.getsource(find_free_port)
        matched_import_socket = re.search(r'import\s*socket', source)
        matched_import_contextlib = re.search(r'from\s*contextlib\s*import\s*closing|'
                                              r'import\s*contextlib\.closing',
                                              source)
        self.assertIsNotNone(matched_import_socket)
        self.assertIsNotNone(matched_import_contextlib)


if __name__ == '__main__':
    unittest.main()
