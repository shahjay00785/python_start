students = []


class Student:

    school_name = "Jeevan Bharti"

    def __init__(self, name, student_id=332):
        self.name = name
        students.append(self)

    def __str__(self):
        return "student " + self.name

    def get_name_captiliaze(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


#jayshah = Student("jay shah")
# print(jayshah)

print(Student.school_name)
