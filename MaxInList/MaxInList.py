# Goldobina Svetlana
#
# find max element and the last its index
while True:
    try:
        # input a list
        lst = input("\n== To close the app input \"exit\" ==\n"
                    "Enter an array of numbers without commas and press enter: ").split()

        # exit mode
        if lst[0] == "exit": exit(0)

        # choose numbers
        lst = list(filter(lambda x: x.isdigit(), lst))
        print("Final array: ", lst)

        # set started values of number and index
        max = lst[0]
        max_index = 0

        # find max and its the last index
        for i in range(0, len(lst)):
            if lst[i] and lst[i] >= max:
                max = lst[i]
                max_index = i

        # print result
        print("max_value:", max, "index:", max_index)

    # empty list, list of chars, punctuations
    except IndexError:
        print("Valid error, try again\n")
        continue