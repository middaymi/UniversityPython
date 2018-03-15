# Goldobina Svetlana
#
# find "time" word in the string
# only single world (not contains in other)
# время
# времени
# времем
# времени
# временами
# временный
# временной

import re

str1 = "какое замечательное время безовремени надо временем и временами без временный и временной период одколовремени"
str2 = "нет совсем времени"
str3 = "просто нет"
str4 = "тесттестВремяВремя"
str5 = "уж очень дорогой ресурс этот, Время"
test_strings = [str1, str2, str3, str4, str5]


def find_time(string):
    pattern = "\\b[Вв]рем\\w+"
    print(re.findall(pattern, string))


if __name__ == "__main__":
    for i in test_strings:
        find_time(i)



