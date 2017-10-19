def is_point_in_area(i, j):
    return (4 >= pow(abs(i + 1), 2) + pow(abs(j - 1), 2) and
        (j >= 2 * i + 2) and
        (j >= -i) or
        (4 == pow(abs(i + 1), 2) + pow(abs(j - 1), 2)) or not
        (4 >= (abs(x + 1) ** 2) + (abs(y - 1) ** 2))) and \
        (y <= 2 * x + 2) and \
        (y <= -x)


def check(s):
    if s.__contains__("exit"): exit(0)
    elif s.isdigit: return float(s)


while True:
    print("\nTo exit enter \"exit\"\nOr enter x y coordinates")
    try:
        x = check(input("x: "))
        y = check(input("y: "))
        print("YES" if is_point_in_area(x, y) else "NO")
    except ValueError:
        print("enter \"exit\" or digits")