import unittest
import socket
from get_master import find_free_port


class TestFindFreePort(unittest.TestCase):
    def test_port_is_free(self):
        # Test that the returned port is actually free.
        port = find_free_port()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            self.assertNotEqual(s.connect_ex(('localhost', int(port))), 0)

    def test_port_is_str(self):
        # Test that the returned port is an integer.
        port = find_free_port()
        self.assertIsInstance(port, str)

    def test_port_in_range(self):
        # Test that the returned port is within the valid range (1024-65535).
        port = find_free_port()
        self.assertTrue(1024 <= int(port) <= 65535)

    def test_multiple_ports_unique(self):
        # Test that calling the function multiple times returns different ports.
        ports = set()
        for _ in range(10):  # Call the function 10 times to test.
            port = find_free_port()
            self.assertNotIn(port, ports)
            ports.add(port)

    def test_reuse_port(self):
        # Test that the function can be called again after a previous call.
        port1 = find_free_port()
        port2 = find_free_port()
        self.assertNotEqual(port1, port2)

if __name__ == '__main__':
    unittest.main()