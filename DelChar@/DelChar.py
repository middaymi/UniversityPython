# Goldobina Svetlana
#
# Delete the character which index %3 == 0

while True:
    # input string
    str = input("\nTo exit enter 0\nOr enter a string: ")

    # if want to exit
    if str.isdigit() and int(str) == 0: exit(0)

    # Up characters
    str = str.replace("@", "")

    print(str)