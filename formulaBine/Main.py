import math

n = input("enter a number: ")
if n.isdigit():
    n = int(n)
    b = (1 + math.sqrt(5)) / 2
    # u = round((b ** n - (-b ** (-n))) / (2 * b - 1))
    u = (b ** n - (-b ** (-n))) / (2 * b - 1)
    u = int(u + 0.5) # для округления
    print(u)
else:
    exit(1)
