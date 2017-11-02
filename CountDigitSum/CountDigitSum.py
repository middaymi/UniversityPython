# Goldobina Svetlana
#
# Counting the amount of the input number

from functools import reduce

while True:
    try:
        # input a number
        input_digit = (input("\nEnter 0 to exit\nOr a number: "))

        # exit mode
        if int(input_digit) == 0: exit(0)

        # print a sum of digits
        print(reduce(lambda x, y: x + y, list(map(lambda x: int(x), input_digit))))

    except ValueError:
        # if input not a number
        print("Enter a number, try again.")
