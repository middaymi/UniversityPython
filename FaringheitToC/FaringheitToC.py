import re


def convert_to_c(item):
    string = str(round(((float(re.sub(r"(\d+)[F|f]", r"\1", item).replace(",", "."))) - 32) / 1.8, 2)).replace(".0", "") + "C"
    return string


def find_faring(string):
    pattern = re.compile(r'(\d+[.|,]*\d*[F|f])')
    circle = re.finditer(pattern, string)
    for item in circle:
        string = re.sub(item.group(), convert_to_c(item.group()), string)
    return string
