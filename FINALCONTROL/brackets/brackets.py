import re


def check(input_str):
    pull = []
    lst = re.sub(r'[\w|\s|\[|\]]*', ' ', input_str.strip()).split()
    print(lst)
    for i in lst:
        if i == '(' or i == '{':
            if len(pull) == 0:
                pull.append(i)
        else:
            if len(pull) != 0:
                pull.clear()
            else:
                if i == "}" and pull[:-1] == "{" or i == ")" and pull[:-1] == "(":
                    pull.remove(pull[:-1])
    return 0 if len(pull) == 0 else 1


# 0
str1 = "ks{sdjkhf( jhkj( {} kjkj( }))){jhgjvj gh}"
print(str1)
print(check(str1))

# 0
str2 = "skd sdufd9fsd f ds][ {lskmdfs  fdlsd} sk ({(}))"
print(str2)
print(check(str2))

# 1
str3 = "kjdfh s[dsf}(lkdsl) {ldmlskm{sklds"
print(str3)
print(check(str3))


