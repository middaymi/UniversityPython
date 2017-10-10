while True:
    input_str = input("To exit enter 0\nOr enter two words separated by a space: ")

    if input_str.isdigit() and int(input_str) == 0: exit(0)
    elif len(input_str.split()) != 2:
        print("Try again. Enter two words separated by a space: ")
        continue
    else: print(' '.join(input_str.split()[::-1]))