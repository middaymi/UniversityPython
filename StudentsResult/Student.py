class Student:

    def __init__(self, *args):
        if len(args) == 4:
            self.name = args[0]
            self.grade = args[1]
            self.mark1 = int(args[2])
            self.mark2 = int(args[3])

    def __str__(self):
        return self.name + " " + self.grade + " " + str(self.mark1) + " " + str(self.mark2)

    def __repr__(self):
        return str(self)

    def count_aver_mark(self):
        return (self.mark1 + self.mark2) / 2
