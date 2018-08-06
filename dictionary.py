student = {
    "name": "mark",
    "student_id": 15163,
    "feedback": None
}

print(student.keys())
print(student.values())
print(student["name"])
student.get("lastname", "Unknown")

all_studetnts = [
    {"name": "Mark", "student_id": 15163, },
    {"name": "katarina", "student_id": 15152},
    {"name": "Jessica", "student_id": 30520}
]
