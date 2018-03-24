import fnmatch
import os
import sys


def find_files(path):
    files_array = []
    try:
        for file in os.listdir(path):
            if fnmatch.fnmatch(file, "*.*[!exe|com|js]"):
                files_array.append(path + file)
        return files_array
    except FileNotFoundError:
        raise FileNotFoundError("Empty or incorrect path")


if __name__ == "__main__":
    path = sys.argv[1]
    find_files(path)