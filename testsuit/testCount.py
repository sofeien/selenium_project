import unittest
import sys
sys.path.append("../")

test_dir = "./"
discover = unittest.defaultTestLoader.discover(test_dir,"test*.py")

if __name__=="__main__":
    unittest.TextTestRunner().run(discover)
