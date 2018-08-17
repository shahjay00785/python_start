students = []


class Student:
    # def add_student(self, name, student_id=332):
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "student" + self.name

    def get_name_capitalization(self):
        return self.get_name_capitalization()

    def get_school_name(self):
        return self.get_school_name

    class HighSchoolStudent(Student):
        school_name = "Jeevan Bharati"

    jayshah = HighSchoolStudent("jay shah")
    print(jayshah.get_name_capitalization())
