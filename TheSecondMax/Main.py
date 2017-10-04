# Goldobina Svetlana
#
# Find the second maximum value in an array

while True:
    lst = input("Enter an array of natural numbers: ").strip().split()

    # if array is empty or entered '0'
    if len(lst) == 0 or ((len(lst) == 1) and (int(lst[0]) == 0)):
        print("GOODBUY")
        exit(0)

    # check an array for numeric values
    for i in lst:
        if not i.isdigit():
            print("%s is not a natural digit! error!" % i)
            exit(0)

    # change to numeric list from input string
    lst = list(map(int, lst))

    # find the second maximum value
    max_1 = max_2 = 0
    for i in lst:
        if i > max_1:
            max_2 = max_1
            max_1 = i
        elif max_2 < i:
            max_2 = i
    print(max_2)

