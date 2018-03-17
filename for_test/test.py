input_lst = []

try:
    while True:
        current = int(input())
        print(current)
        if current != 0:
            input_lst.append(current)
        else:
            break
except ValueError:
    print("Enter numbers! Try again.")
