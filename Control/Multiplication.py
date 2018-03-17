# 1×2+2×3+...+(n-1)×n

input = int(input("value: "))
sum = 0
for i in range(1, input):
    end = ' + '
    inp_sum = ''
    sum += (i * (i + 1))
    if i == input - 1:
        end = ''
        inp_sum = ' = ' + str(sum)
    print(i, '*', i+1, inp_sum, sep='', end=end)
