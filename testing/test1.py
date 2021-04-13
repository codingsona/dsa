import unittest

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

boolean = True


class TestAll(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2, 2)
        self.assertEqual(add(2, 4), 6)
        self.assertNotEqual(add(2,4), 10)

    def test_bool(self):
        self.assertTrue(boolean)
        #self.assertFalse(boolean)

    def test_subtract(self):
        self.assertEqual(subtract(30, 10), 20)

if __name__ == "__main__":
    unittest.main()



