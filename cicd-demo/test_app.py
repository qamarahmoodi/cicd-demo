import unittest

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

class TestApp(unittest.TestCase):
    def test_add(self):
        assert add(2, 3) == 5

    def test_is_even(self):
        assert is_even(4)

if __name__ == "__main__":
    unittest.main()