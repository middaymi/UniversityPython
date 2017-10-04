# Goldobina Svetlana
#
# Translate decimal number < 16 into binary code
# and count "1" value in translation


# translate decimal number into binary code and count "1"
def to_binary(number):
    input_number = number
    binaries = []
    result_string = ""
    rest = -1

    while number > 1:
        rest = number % 2
        binaries.append(rest)
        number = int(number / 2)
    binaries.append(number)
    binaries.reverse()

    for i in binaries:
        result_string = result_string + str(i)

    print("binary code of %d is %r and numbers of \"1\" = %d"
          % (input_number, result_string, binaries.count(1)))


while True:
    input_number = input("Enter natural number n < 16: ").strip()
    if input_number.isdigit():
        input_number = int(input_number)
        if input_number == 0:
            break
            exit(0)
        if input_number < 16:
            to_binary(input_number)
            print("\n")
        else:
            print("Error! Entered number > 16!\n")
    else:
        print("Error! Incorrect entered value!")
