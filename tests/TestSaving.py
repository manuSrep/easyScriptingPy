
import unittest
import sys
import os
import shutil

sys.path.append("../miscpy/")
from miscpy import prepareSaving, extractFromFilename


class TestExtractFromFilename(unittest.TestCase):

    def test_filename_including_path_name_ext(self):
        test_file = ["path/file.ext"]
        expected_name = ["file"]
        expected_path = ["path"]
        expected_ext = ["ext"]
        for f, file in enumerate(test_file):
            fname, path, ext = extractFromFilename(file)
            self.assertEqual(fname, expected_name[f])
            self.assertEqual(path, expected_path[f])
            self.assertEqual(ext, expected_ext[f])

    def test_filename_including_extension(self):
        test_file = ["file.ext"]
        expected_name = ["file"]
        expected_path = [""]
        expected_ext = ["ext"]
        for f, file in enumerate(test_file):
            fname, path, ext = extractFromFilename(file)
            self.assertEqual(fname, expected_name[f])
            self.assertEqual(path, expected_path[f])
            self.assertEqual(ext, expected_ext[f])

    def test_filename_including_path_only(self):
        test_file = ["path/"]
        expected_name = [""]
        expected_path = ["path"]
        expected_ext = [""]
        for f, file in enumerate(test_file):
            fname, path, ext = extractFromFilename(file)
            self.assertEqual(fname, expected_name[f])
            self.assertEqual(path, expected_path[f])
            self.assertEqual(ext, expected_ext[f])


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
                    new = prepareSaving(name, os.path.join("delete_me", path), ext)
                    self.assertEqual(control, new)
                    self.assertTrue(os.path.exists(os.path.abspath(os.path.join("delete_me", path))))

    def test_filename_from_name_including_path_and_extension(self):
        test_name = ["path/file.ext"]
        test_path = ["path", "path/path", "path//path"]
        for name in test_name:
            for path in test_path:
                control = os.path.abspath(os.path.join("delete_me", os.path.join(path, "{n}".format(n=name))))
                new = prepareSaving(name, os.path.join("delete_me", path))
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
                    new = prepareSaving(name, os.path.join("delete_me", path), ext)
                    self.assertEqual(control, new)
                    self.assertTrue(os.path.exists(os.path.abspath(os.path.join("delete_me", path))))

    def test_filename_including_path_only(self):
        test_name = ["path/path/"]
        for name in test_name:
            control = os.path.abspath(os.path.join("delete_me",name)) + "/"
            new = prepareSaving(os.path.join("delete_me", name))
            self.assertEqual(control, new)
            self.assertTrue(os.path.exists(os.path.abspath(os.path.join("delete_me", name))))


    def doCleanups(self):
        shutil.rmtree("delete_me/")


if __name__ == '__main__':
    unittest.main()