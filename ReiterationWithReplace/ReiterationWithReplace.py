import re

#
# def find_repeatable_world(str):
#     p = re.compile(r'\b(\w+)\s+\1\b')
#     print(p.findall(str))


# def del_repeats(lst):
#
#
#     p = re.compile(r'\b(\w+)\s+\1\b')
#     string = re.sub(p, "", string)
#     print(string)


# find_repeatable_world("ла ла ло ло ла")
# p = re.compile(r'\b(\w+)\s+\1\b')
# string = re.sub(p, "", string)
# print(string)

string = "ла ла ло ло ла"
p = re.compile(r'\b(\w+)\s+\1\b')
# print(p.findall(string))
string = re.sub(p, "\1", string)
print(string)
