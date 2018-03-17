# Goldobina Svetlana
#
# check that an input point in square


# check a point in square
def is_point_in_square(i, j):
    return abs(i) + abs(j) <= 1


# check an input value
def check(s):
    if "exit" in s: exit(0)
    elif s.isdigit: return float(s)


while True:
    print("\nTo exit enter \"exit\"\nOr enter x y coordinates")
    try:
        x = check(input("x: "))
        y = check(input("y: "))
        print(str(is_point_in_square(x, y)).replace("True", "YES").replace("False", "NO"))
    except ValueError:
        print("enter \"exit\" or digits")

