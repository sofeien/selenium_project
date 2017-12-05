import unittest
from count import Count

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("begin test sub function")
    def test_sub(self):
        self.assertEqual(Count().sub(2,3),-1)
    def test_add2(self):
        self.assertEqual(Count().sub(3,2),1)
    def tearDown(self):
        print("end test sub function")

if __name__ == "__main__":
    unittest.main()
