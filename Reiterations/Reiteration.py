import re


def find_repeatable_world(str):
    p = re.compile(r'\b(\w+)\s+\1\b')
    return p.findall(str)