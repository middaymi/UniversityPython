str1 = "laladon"
str2 = "lalalend"

len1 = len(str1)
len2 = len(str2)
final = len2 if (len1 > len2) else len1
counter = 0

for i in range(0, final):
    if str1[i] == str2[i]:
        counter += 1
    else:
        break
print(counter)
