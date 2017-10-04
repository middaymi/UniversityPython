# Goldobina Svetlana
#
# find local maximums in an array
# local maximum - the number which is greater than its neighbor
# border values ​​are compared with one neighbor


while True:

    # getting a list as str from keyboard
    lst = (input("\nFor exit enter 0 \nOr enter an array of natural numbers: ").strip().split())

    # exit mode
    if lst[0] == '0': exit(0)

    try:
        # to do an array of numeric values
        lst = list(map(int, lst))
        print(lst)
        ll = len(lst)

        # create an array of the local max indexes
        index_lst = []

        # find local maximums and add them to the array of indexes
        for i in range(0, ll):
            if i == 0 and lst[0] > lst[1]: index_lst.append(0)
            elif i == ll - 1 and lst[ll - 1] > lst[ll - 2]: index_lst.append(ll - 1)
            elif lst[i - 1] < lst[i] > lst[i + 1]: index_lst.append(i)
        print(index_lst)
        li = len(index_lst)

        # find min range of the local maximums indexes
        if li != 1:
            min_range = index_lst[1] - index_lst[0]
            for i in range(1, li):
                tmp = index_lst[i] - index_lst[i - 1]
                if tmp < min_range: min_range = tmp
        # if one number range = 0
        else:
            min_range = 0
        print(min_range)

    except ValueError:
        print("Incorrect values! Try again!")
