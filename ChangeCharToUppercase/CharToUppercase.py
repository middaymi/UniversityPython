# Goldobina Svetlana
#
# Change H to h except the first and the last h-element

while True:
    # input a string
    str = input("\nTo exit enter 0\nOr enter a string: ")

    # exit
    if str.isdigit() and int(str) == 0: exit(0)

    # find the first and the last index of h-element
    left = str.find('h')
    right = str.rfind('h')

    # print modify string
    print(str[0:left+1] + str[left+1:right].replace("h", "H") + str[right:len(str)])






















# # Goldobina Svetlana
# #
# # Delete the character which index %3 == 0
#
# while True:
#     # input string
#     str = input("\nTo exit enter 0\nOr enter a string: ")
#
#     # if want to exit
#     if str.isdigit() and int(str) == 0: exit(0)
#
#     # Up characters
#     str = str.replace("h", "H")
#
#     print(str)