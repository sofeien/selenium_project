import unittest
from count import Count

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("begin test add function")
    def test_add(self):
        self.assertEqual(Count().add(2,3),5)
    @unittest.skipUnless(3>2,"jump")
    def test_add2(self):
        self.assertEqual(Count().add(3,2),5)
    def tearDown(self):
        print("end test add function")

if __name__ == "__main__":
    unittest.main()
        
