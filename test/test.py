def fib(n):
    f1, f2 = 0, 1
    for i in range(n):
        f1, f2 = f2, f1 + f2
        yield f1


for i in fib(20):
    print(fib, end=' ')
print()

print("Cумма первых 100 чисел Фибоначчи равна", sum(fib(100)))
print(list(fib(16)))
print([x * x for x in fib(14)])
