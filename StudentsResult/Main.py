from Student import Student

listOfStudents = []
txt_file = open(file="results.txt", encoding="utf-8")
for line in txt_file.readlines():
    listOfStudents.append(Student(*line.split()))

for student in listOfStudents:
    print(student.name, student.count_aver_mark())

