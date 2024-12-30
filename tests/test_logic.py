from logic import work, short, long
import unittest

class TestLogicFunctions(unittest.TestCase):
    def test_work(self):
        self.assertEqual(work(), "25:00")

    def test_short(self):
        self.assertEqual(short(), "5:00")

    def test_long(self):
        self.assertEqual(long(), "15:00")

if __name__ == "__main__":
    unittest.main()