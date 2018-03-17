import os

path = "./goods"
dirFiles = os.listdir(path)
txtFiles = []
goods = set()

for fileName in dirFiles:
    if fileName.endswith(".txt"):
        txtFiles.append(fileName)

for fileName in txtFiles:
    file = open(path + "//" + fileName, "r")
    for line in file.readlines():
        goods.add(line.split(",")[0])
print("НАйдено товаров:", goods)

