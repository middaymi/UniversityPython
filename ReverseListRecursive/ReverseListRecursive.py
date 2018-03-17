def fun(list, i):
    if i == len(list) - 1:
        return
    list[i - 1], list[-i] = list[-i], list[i - 1]
    fun(list, i + 1)


lst = [1, 3, 5, 6, 7]
# lst2 = []
fun(lst, 1)
print(lst)




















# def reverse(index):
#     lenDesc = len - index - 1
#     if  index - (len - index) >= 0:
#         return 1
#     else:
#         lst[index], lst[lenDesc] = lst[lenDesc], lst[index]
#
#
# for i in range(0, len//2):
#     reverse(i)
# print(lst)