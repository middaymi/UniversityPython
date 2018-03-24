import unittest
import FaringheitToC


class Tests(unittest.TestCase):

    def setUp(self):
        str1 = "gg 56,6F ccj 88.7F"
        str2 = "56.6F 5F 88,7F"
        str3 = "F 87hggfF"
        str4 = ""
        self.array_of_strings = [str1, str2, str3, str4]

        res1 = "gg 13.67C ccj 31.5C"
        res2 = "13.67C -15C 31.5C"
        res3 = "F 87hggfF"
        res4 = ""
        self.array_of_res = [res1, res2, res3, res4]

    def test_find_faring_function(self):
        for i in range(0, len(self.array_of_strings)):
            self.assertEqual(self.array_of_res[i], FaringheitToC.find_faring(self.array_of_strings[i]),
                             "Fail in function find_faring() with {0} argument".format(self.array_of_strings[i]))


if __name__ == '__main__':
    unittest.main()
