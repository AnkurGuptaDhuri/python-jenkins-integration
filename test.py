import unittest
# This is the class we want to test. So, we need to import it
from calc import calculator


class test_calculator(unittest.TestCase):
    def test_add_positive(self):
        calc1 = calculator(12,10)
        result = calc1.add()
        self.assertEqual(result, 22)

    def test_add_negative(self):
        calc1 = calculator(12,-10)
        result = calc1.add()
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
