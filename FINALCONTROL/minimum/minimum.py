def find_mimimum(biglist, k):
    min_index = 0
    min_value = 0
    for i in range(0, len(biglist) - k + 1):
        smalllist = biglist[i:k + i]
        if i == 0 or min_index < i:
            min_value = min(smalllist)
            min_index = smalllist.index(min_value)
        else:
            if smalllist[len(smalllist) - 1] < min_value:
                min_value = smalllist[len(smalllist) - 1]
                min_index = len(smalllist) - 1
        print(min_value)
    print()


# 2, 6, 7, 4, 4, 4, 4
lst1 = [2, 6, 7, 8, 9, 22, 4, 6, 7, 8]
find_mimimum(lst1, 4)

# 0 0 0 0
lst2 = [0, 4, 0, 8, 9, 0, 33, 5, 6]
find_mimimum(lst2, 6)






