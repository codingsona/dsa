import unittest
import testing.test1


class TestAdd(unittest.TestCase):
    def setUp(self):
        self.number = None
        self.boolean = True
        self.a = 5
        self.b = 6

    def test_add(self):
        #self.assertEqual(2, 2)
        self.assertEqual(testing.test1.add(self.a, self.b), 11)
        self.assertNotEqual(testing.test1.add(2,4), 10)

    def test_bool(self):
        self.assertTrue(testing.test1.boolean)
        #self.assertFalse(testing.test1.boolean)

    def test_subtract(self):
        self.assertEqual(testing.test1.subtract(30, 10), 20)
        self.assertEqual(testing.test1.subtract(self.a, self.b), -1)

    def tearDown(self):
        print(self.boolean)
        del self.boolean



if __name__ == "__main__":
    unittest.main()
