import shutil
import unittest
import os
import FindNotExecutableFiles
from pathlib import Path


class Tests(unittest.TestCase):

    def setUp(self):
        self.new_dir = os.getcwd() + "/files/"

    def test_with_response(self):
        os.mkdir(self.new_dir)
        print(self.new_dir)
        Path(self.new_dir + "/text1.txt").touch()
        Path(self.new_dir + "/text2.csv").touch()
        Path(self.new_dir + "/text3.exe").touch()
        Path(self.new_dir + "/text4.com").touch()
        Path(self.new_dir + "/text5.js").touch()
        request_array = [self.new_dir + "text1.txt",
                         self.new_dir + "text2.csv"]
        self.assertEqual(request_array, FindNotExecutableFiles.find_files(self.new_dir))

    def test_without_response(self):
        os.mkdir(self.new_dir)
        Path(self.new_dir + "/text1.exe").touch()
        Path(self.new_dir + "/text2.js").touch()
        Path(self.new_dir + "/text3.exe").touch()
        Path(self.new_dir + "/text4.com").touch()
        Path(self.new_dir + "/text5.js").touch()
        request_array = []
        self.assertEqual(request_array, FindNotExecutableFiles.find_files(self.new_dir))

    def test_empty_path(self):
        self.new_dir = ""
        self.assertRaises(FileNotFoundError, FindNotExecutableFiles.find_files, self.new_dir)

    def test_incorrect_path(self):
        self.new_dir = "lala"
        self.assertRaises(FileNotFoundError, FindNotExecutableFiles.find_files, self.new_dir)

    def tearDown(self):
        shutil.rmtree(self.new_dir, ignore_errors=True)


if __name__ == '__main__':
    unittest.main()
