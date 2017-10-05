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
        if i < 0 or i >= 8:
            print("Number %d not in range[0, 7]. Try again!" % i)
            return 1


while True:
    # get coordinates
    print("\nTo exit enter 0\nOr enter coordinates by space and value = [0,7] and the format is: x y")
    current = (input("Current position: ")).strip().split()
    wish = (input("Desired position: ")).strip().split()

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
    if -1 <= current[0] - wish[0] <= 1 and -1 <= current[1] - wish[1] <= 1:
        print("YES")
    else:
        print("NO")