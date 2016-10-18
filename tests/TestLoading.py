import unittest
import sys
import os
import shutil

sys.path.append("../miscpy/")
from miscpy import prepareLoading, multiLoading


class TestPrepareSaving(unittest.TestCase):

    def setUp(self):
        if not os.path.exists("delete_me"):
            os.makedirs("delete_me/")


    def test_filename_from_name_path_and_extension(self):
        test_name = ["file"]
        test_path = ["path", "path/path", "path//path"]
        test_ext = ["ext", ".ext"]
        for name in test_name:
            for path in test_path:
                for ext in test_ext:
                    control = os.path.abspath(os.path.join("delete_me", os.path.join(path, "{n}.ext".format(n=name))))
                    if not os.path.exists(os.path.dirname(control)):
                        os.makedirs(os.path.dirname(control))
                    open(control,'a').close()
                    new = prepareLoading(name, os.path.join("delete_me", path), ext)
                    self.assertEqual(control, new)

    def test_filename_from_name_including_path_and_extension(self):
        test_name = ["path/file.ext"]
        test_path = ["path", "path/path", "path//path"]
        for name in test_name:
            for path in test_path:
                control = os.path.abspath(os.path.join("delete_me", os.path.join(path, "{n}".format(n=name))))
                if not os.path.exists(os.path.dirname(control)):
                    os.makedirs(os.path.dirname(control))
                open(control, 'a').close()
                new = prepareLoading(name, os.path.join("delete_me", path))
                self.assertEqual(control, new)
                self.assertTrue(os.path.exists(os.path.abspath(os.path.join("delete_me", path+"/path/"))))

    def test_filename_from_name_overwriting_extension(self):
        test_name = ["file.foo"]
        test_path = ["path", "path/path", "path//path"]
        test_ext = ["ext",  ".ext"]
        for name in test_name:
            for path in test_path:
                for ext in test_ext:
                    control = os.path.abspath(os.path.join("delete_me", os.path.join(path, "file.ext")))
                    if not os.path.exists(os.path.dirname(control)):
                        os.makedirs(os.path.dirname(control))
                    open(control, 'a').close()
                    new = prepareLoading(name, os.path.join("delete_me", path), ext)
                    self.assertEqual(control, new)
                    self.assertTrue(os.path.exists(os.path.abspath(os.path.join("delete_me", path))))

    def test_filename_not_existing(self):
        test_name = ["foo.bar"]
        for name in test_name:
            self.assertRaises(IOError, prepareLoading, name)


    def doCleanups(self):
        shutil.rmtree("delete_me/")


class TestMultiLoading(unittest.TestCase):

    def test_excluding_subdir(self):
        test_files = ["file_test_1.tst", "path/file_test_2.tst", "file_test_3.txt", "file_tet_4.tst"]
        expected_files = ["file_test_1.tst"]

        for file in test_files:
            file = os.path.join("delete_me/", file)
            if not os.path.exists(os.path.dirname(file)):
                os.makedirs(os.path.dirname(file))
            open(file, 'a').close()

        for i in range(len(expected_files)):
            expected_files[i] = os.path.abspath(os.path.expanduser(os.path.join("delete_me", expected_files[i])))
        self.assertEqual(expected_files, multiLoading("*_test_*.tst", "delete_me", SUBPATH=False))

    def test_including_subdir(self):
        test_files = ["file_test_1.tst", "path/file_test_2.tst",
                      "file_test_3.txt", "file_tet_4.tst"]
        expected_files = ["file_test_1.tst", "path/file_test_2.tst"]

        for file in test_files:
            file = os.path.join("delete_me/", file)
            if not os.path.exists(os.path.dirname(file)):
                os.makedirs(os.path.dirname(file))
            open(file, 'a').close()

        for i in range(len(expected_files)):
            expected_files[i] = os.path.abspath(os.path.expanduser(
                os.path.join("delete_me", expected_files[i])))
        self.assertEqual(expected_files, multiLoading("*_test_*.tst", "delete_me", SUBPATH=True))

    def doCleanups(self):
        shutil.rmtree("delete_me/")



if __name__ == '__main__':
    unittest.main()