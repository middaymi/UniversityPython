# Goldobina Svetlana
#
# find local maximums in an array
# local maximum - the number which is greater than its neighbor


# print result and clear data
def print_clear_data(lst, dis):
    if len(lst) != 0:
        print("list:", lst)
        if len(dis) != 0:
            print("distance list:", dis,
                  "\nmin distance:", min(dis))
            dis.clear()
        else:
            print("min distance:", 0)
        lst.clear()


# find min distance between neighbors
def find_min_distance(lst, dis, index):
    for i in range(1, len(lst) - 1):
        if lst[i - 1] < lst[i] > lst[i + 1]:
            if i != 1:
                dis.append(i - index)
            index = i


# getting a list as str from keyboard
def input_check_array(lst):
    print("\nEnter values:")
    while True:
        current = input().strip()
        # exit mode
        if current.strip() == "exit":
            exit(0)

        if int(current) != 0:
            lst.append(int(current))
        else:
            break


array = []
distance = []
index_of_localmax = 0

while True:
    try:
        input_check_array(array)
        find_min_distance(array, distance, index_of_localmax)
        print_clear_data(array, distance)

    except ValueError:
        print("Enter numbers! Try again.")
