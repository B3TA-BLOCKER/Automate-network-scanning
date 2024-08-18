import unittest
from network_scanner.utils import clear_screen

class TestUtils(unittest.TestCase):
    def test_clear_screen(self):
        # This is tricky to test, so you might just test it doesn't throw errors
        try:
            clear_screen()
        except Exception as e:
            self.fail(f"clear_screen raised an exception {e}")

if __name__ == '__main__':
    unittest.main()
