students = []


def get_student_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
        #students_titlecase = student["name"].title()
    print(students_titlecase)


def print_students_titlecase():
    students_titlecase = get_student_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("student.txt", "a")
        f.write(student+"\n")
        f.close()
    except Exception:
        print("could not save the file")


def read_file():
    try:
        f = open("student.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("could not read file")


#student_list = get_student_titlecase()

read_file()
print_students_titlecase()


student_name = input("enter student name->")

student_id = input("enter student id->")

add_student(student_name, student_id)
save_file(student_name)


# print_students_titlecase()
