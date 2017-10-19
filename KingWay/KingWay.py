# Goldobina Svetlana
#
# check the king's ability to move from the
# current to the specified position


# check a number and value of coordinates
def check(lst):

    if len(lst) != 2:
        print("Each position is given by two coordinates! Try again!")
        return 1

    for i in lst:
        if 1 <= i <= 8:
            print("Number %d not in range[1, 8]. Try again!" % i)
            return 1


# check to exit
def to_exit(lst):
    if len(lst) == 1 and int(lst[0]) == 0:
        exit(0)


while True:
    # get coordinates
    print("\nTo exit enter 0\nOr enter coordinates by space and value = [0,7] and the format is: x y")

    current = (input("Current position: ")).strip().split()
    to_exit(current)

    wish = (input("Desired position: ")).strip().split()
    to_exit(wish)

    try:
        # to do numeric lists
        current = list(map(int, current))
        wish = list(map(int, wish))
    except ValueError:
        print("Something wrong with your value(s)! Try again!\n")
        continue

    # check input coordinates
    if check(current) == 1 or check(wish) == 1: continue

    # if the current and desired position are the same
    if current[0] == wish[0] and current[1] == wish[1]:
        print("This is your position!")
        continue

    # all conditions are passed, check new way
    if current[0] - wish[0] <= abs(1) and current[1] - wish[1] <= abs(1):
        print("YES")
    else:
        print("NO")