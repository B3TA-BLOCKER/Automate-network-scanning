import unittest
from network_scanner.scanner import network_interface_info

class TestScanner(unittest.TestCase):
    def test_network_interface_info(self):
        interfaces = network_interface_info()
        self.assertIsInstance(interfaces, list)

if __name__ == '__main__':
    unittest.main()
