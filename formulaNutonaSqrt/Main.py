import math

A = input("enter a number: ")
eps = 0.01
xk = 0

if A.isdigit():
    A = int(A)
    xk1 = A / 2

    while math.fabs(xk1-xk) > eps:
        xk = xk1
        xk1 = 1 / 2 * (xk + A / xk)
    print("кв корень из %d равен %g с точностью %g" % (A, round(xk1, 2), eps))

else:
    exit(1)


