# Goldobina Svetlana
#
# Count unique values in input array

try:
    print(len(set(map(lambda x: int(x, 0), input().split()))))
except ValueError:
    print("invalid values")