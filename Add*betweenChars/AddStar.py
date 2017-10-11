# Goldobina Svetlana
#
# Add * between characters in a word

while True:

    # get a word
    str = input("\nTo exit enter 0\nOr enter a word: ")

    # check a number of words
    if len(str.split()) != 1:
        print("Enter one word, try again")
        continue

    # exit
    elif str.isdigit() and int(str) == 0: exit(0)

    # add * between chars
    print("*".join(list(str)))