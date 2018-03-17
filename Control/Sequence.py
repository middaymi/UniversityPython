dictionary = {}
for i in range(1, 10):
    dictionary.update({i: 0})

print("Input:")
while True:
    current = input().strip()
    current = int(current)
    if current != 0:
        dictionary.update({current: dictionary.get(current) + 1})
    else:
        break

for i in dictionary:
    print(dictionary.get(i), sep='', end='')

