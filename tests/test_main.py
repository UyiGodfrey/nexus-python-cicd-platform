import unittest
from app.main import calculate_balance

class TestBalance(unittest.TestCase):
    def test_balance(self):
        self.assertEqual(calculate_balance(5000, 2000), 3000)

if __name__ == "__main__":
    unittest.main()
