import re


def find_repeatable_world(string):
    p = re.compile(r'\b(\w+)\b\s+\b\1\b')
    return re.sub(p, r'\1', string)