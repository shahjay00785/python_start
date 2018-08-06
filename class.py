students = []


class Student:
    # def add_student(self, name, student_id=332):
    def __init__(self, name, student_id=332):
        student = {"name": name, "student_id": student_id}
        students.append(student)

    def __str__(self):
        return "student"


jayshah = Student("jay shah")
print(jayshah)

"""
student = Student()
student.add_student("Mark")
"""
# print(students)
