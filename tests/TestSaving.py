import unittest
import sys
import os
import shutil

sys.path.append("../easyScripting")
from Saving import prepareSaving



class TestPrepareSaving(unittest.TestCase):

    def setUp(self):
        self.test_path = 'path'
        self.test_name = "name"

    def test_extension(self):
        extension = "tst"
        print(prepareSaving(self.test_name,self.test_path,extension))

    def test_dot_extension(self):
        extension = ".tst"
        print(prepareSaving(self.test_name,self.test_path,extension))

    def test_complex_path(self):
        path = self.test_path + "/path_sub/"
        extension = ".tst"
        print(prepareSaving(self.test_name,path,extension))


    def doCleanups(self):
        shutil.rmtree(self.test_path)


if __name__ == '__main__':
    unittest.main()