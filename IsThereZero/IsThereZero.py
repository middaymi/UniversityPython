# Goldobina Svetlana
#
# find zero in input array
# to stop input values press command/control D


import sys

print("True" if len(list(filter(lambda x: x == '0', sys.stdin.read().strip().split('\n')))) > 0 else "False")