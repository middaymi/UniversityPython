# Goldobina Svetlana
#
# to calculate the end time of the lesson

while True:
    try:
        # input value
        lesson = input("lesson: ")

        # exit mode
        if lesson == "exit": exit(0)

        lesson = int(lesson)

        # check value
        # value > 16 is bad because of the end a time of day
        if 0 >= lesson or lesson > 16:
            print("Enter a 0 < natural number <= 16\n")
            continue

        # count time
        minutes = 45 * lesson + 5 * int(lesson / 2) + 15 * int((lesson - ((lesson - 1) % 2)) / 2)
        print(9 + int(minutes / 60), ":", minutes - int(minutes / 60) * 60, "\n")

    except ValueError:
        print("Enter a natural number > 0\n")