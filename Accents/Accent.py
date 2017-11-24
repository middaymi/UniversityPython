# coding=utf-8
from __future__ import print_function, with_statement


def is_one_upper_letter(word):
    count = 0
    for letter in word:
        if letter.isupper():
            count = count + 1
    if count == 1:
        return True
    return False


dictionary = dict()

with open("text.txt", 'r') as file:
    dict_size = int(file.readline())
    for x in range(dict_size):
        word = file.readline()
        word = word.strip()
        lower_world = word.lower()
        if lower_world in dictionary:
            dictionary[lower_world].append(word)
        else:
            dictionary[lower_world] = [word]
    hw = file.readline()

hw = hw.strip()
error = 0
for case in hw.split(' '):
    if not case.isspace():
        lcase = case.lower()
        if lcase in dictionary:
            if case in dictionary[lcase]:  # a word with accent is in dictionary
                continue
            else:
                error = error + 1  # there are worlds in dictionary, but without needed accent
        else:  # if there isn't a word in dictionary, maybe incomplete dictionary
            if is_one_upper_letter(case):
                continue
            else:
                error = error + 1
print(error)



