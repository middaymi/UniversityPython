# Goldobina Svetlana
#
# Delete a character @

while True:
    # input a string
    str = input("\nTo exit enter 0\nOr enter a string: ")

    # exit case
    if str.isdigit() and int(str) == 0: exit(0)

    # delete @
    str = str.replace("@", "")

    print(str)