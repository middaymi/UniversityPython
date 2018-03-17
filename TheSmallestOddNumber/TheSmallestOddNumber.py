# Goldobina Svetlana
#
# find the smallest odd number in input list


print(min([x for x in list(map(int, input().split())) if x % 2 != 0]))

