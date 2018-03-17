import unittest
import Reiteration


class Tests(unittest.TestCase):

    def setUp(self):
        str1 = "тест тест и тестовая среда"
        str2 = "тест и тест"
        str3 = ""
        str4 = "про тест и и просто просто тест"
        self.array_of_strings = [str1, str2, str3, str4]

        res1 = ["тест"]
        res2 = []
        res3 = []
        res4 = ["и", "просто"]
        self.array_of_results = [res1, res2, res3, res4]

    def test_function(self):
        for i in range(0, len(self.array_of_strings)):
            self.assertEqual(self.array_of_results[i], Reiteration.find_repeatable_world(self.array_of_strings[i]),
                             "Wrong value in test string \"{0}\"!".format(self.array_of_strings[i]))


if __name__ == '__main__':
    unittest.main()