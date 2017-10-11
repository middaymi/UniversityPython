# Goldobina Svetlana
#
# Delete the character which index %3 == 0

while True:
    # input string
    str = input("\nTo exit enter 0\nOr enter a string: ")

    # if not one word
    if len(str.split()) != 1:
        print("Enter one word, try again")
        continue

    # if want to exit
    elif str.isdigit() and int(str) == 0: exit(0)

    # del characters
    str = ''.join([x for x in str if x != "@"])
    print(str)