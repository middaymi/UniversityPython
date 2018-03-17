# Goldobina Svetlana
#
# count the composition of the fifth power of each number

from functools import reduce

try:
    print(reduce(lambda x, y: x * y, list(map(lambda x: int(x)**5, input().strip().split()))))
except TypeError:
    print("No values")