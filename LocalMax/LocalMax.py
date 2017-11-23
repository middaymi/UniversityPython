# Goldobina Svetlana
#
# find local maximums in an array
# local maximum - the number which is greater than its neighbor


def print_result(lst, min):
    print("list =", lst)
    print("min distance =", min, "\n***\n")


# getting a list as str from keyboard
def input_check_array(lst):
    print("Input:")
    while True:
        current = input().strip()
        # exit mode
        if current.strip() == "exit":
            exit(0)
        if int(current) != 0:
            lst.append(int(current))
        else:
            break


while True:
    index_localmax = -1
    min_dist = 0
    list = []
    try:
        input_check_array(list)
        # find min distance between neighbors
        for i in range(1, len(list) - 1):
            if list[i - 1] < list[i] > list[i + 1]:
                if index_localmax != -1:
                    dist = i - index_localmax
                    if min_dist > dist or min_dist == 0:
                        min_dist = dist
                index_localmax = i
        print_result(list, min_dist)
    except ValueError:
        print("Enter numbers! Try again.")