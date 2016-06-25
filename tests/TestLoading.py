import unittest
import sys
import os
import shutil

sys.path.append("../easyScripting")
from Loading import prepareLoading, multiLoading



class TestPrepareLoading(unittest.TestCase):

    def setUp(self):
        self.test_path = "path/"
        self.test_name = "name"
        self.test_extension = ".tst"
        os.makedirs(self.test_path)
        open(self.test_path+self.test_name+self.test_extension, 'w+')

    def test_extension(self):
        extension = ".tst"
        print(prepareLoading(self.test_name,self.test_path,extension))

    def test_dot_extension(self):
        extension = ".tst"
        print(prepareLoading(self.test_name,self.test_path,extension))

    def test_complex_path(self):
        try:
            path = self.test_path + "/path_sub/"
            extension = ".tst"
            print(prepareLoading(self.test_name, path, extension))
        except IOError:
            print ('IOError successful')

    def doCleanups(self):
        shutil.rmtree(self.test_path)


class TestMultiLoading(unittest.TestCase):

    def setUp(self):
        self.test_subpath = "sub_path/"
        self.test_path = "path/"
        self.test_name = "name"
        self.test_extension = ".tst"
        os.makedirs(self.test_path+self.test_subpath)
        for i in range(10):
            open(self.test_path+self.test_name+"_{i}".format(i=i)+self.test_extension, 'w+')
            open(self.test_path+self.test_name+"_{i}".format(i=i)+".png", 'w+')
            open(self.test_path+ self.test_subpath+self.test_name + "_{i}".format(
                i=i) + self.test_extension, 'w+')

    def test_with_subdir(self):
        print(multiLoading(directory=self.test_path, SUBDIRS=True, extension=self.test_extension))

    def test_without_subdir(self):
        print(multiLoading(directory=self.test_path, SUBDIRS=False, extension=self.test_extension))

    def test_include_all(self):
        print(multiLoading(directory=self.test_path, SUBDIRS=False))


    def doCleanups(self):
        shutil.rmtree(self.test_path)

if __name__ == '__main__':
    unittest.main()
