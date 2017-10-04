# Goldobina Svetlana
#
# get the number of the day when the athlete ran or will run
# the entered number of kilometers
#
# enter "x" - the number of kilometers that ran on the first day
# and "y" - other number of kilometers; x and y are real numbers
# "day" - the day when the athlete ran or will run at least a certain number of kilometers

import math

while True:
    try:
        # getting the number of kms running at the first day
        # and check for the desire to leave
        print("If you want to exit print 000")
        x = float(input("Enter the number of kms that have run the first day: ").strip())
        if x == 0:
            exit(0)

        # getting the number of the next days
        # and check for the desire to leave
        y = float(input("Enter the number of kms that have run the next days: ").strip())
        if y == 0:
            exit(0)

        # calc a day
        if x == y:
            day = 1
        else:
            day = round((math.log(y / x, 1.1) + 1) + 0.5)

        # if the second value was bigger the first
        if day < 0:
            print("Something went wrong, check your entered values!\n")
            continue

        # if everything is fine
        print("Day:", day, "\n")

    # if the values ​​were incorrect
    except ValueError:
        print("Entered value(s) are not numbers! Try again!\n")

