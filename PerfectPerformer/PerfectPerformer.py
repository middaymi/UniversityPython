# Goldobina Svetlana
#
# getting b from a by the shortest path using the deduction 1 and division in half
# numbers are natural and with the condition that A > B

while True:

    print("\nTo exit enter 0 \nOr enter two natural numbers A > B")

    try:
        # enter A and B
        # check for the desire to leave
        a = int(input("A: "))
        if a == 0: exit(0)

        b = int(input("B: "))
        if b == 0: exit(0)

        # if condition that A > B is not met
        if a < b:
            print("The condition that A > B")
            continue

        # if all is normal
        while a != b:

            # at first divide
            if (a % 2 == 0) and (a / 2 >= b):
                a = a / 2
                print(":2\n")

            # if can not divide, to do -1
            else:
                a = a - 1
                print("-1\n")

    # if input value error
    except ValueError:
        print("Something wrong with your input value(s)! Try again.")
