import unittest
import sys
import os

sys.path.append("../fileHandler")
from Saving import prepareSaving



class TestPrepareSaving(unittest.TestCase):

    def setUp(self):
        self.fname = "name"
        self.path = "path"
        self.extension = ".tst"


    def test_prepareSaving(self):
        print(prepareSaving(self.fname,self.path,self.extension))
        print(self.fname)


    def doCleanups(self):
        os.removedirs("path")


if __name__ == '__main__':
    unittest.main()