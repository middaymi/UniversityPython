def Election(x, y, z):
    lst = [x, y, z]

    one = 0
    zero = 0

    for i in lst:
        i = int(i)
        if i == 0:
            zero += 1
        else: one += 1

    if one > zero: print("1")
    else: print("0")


Election(*(input("values: ").strip().split()))






