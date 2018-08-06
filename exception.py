student = {
    "name": "mark",
    "student_id": 21355,
    "feedback": None
}

student["last_name"] = "kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error Finding last_name")
except TypeError as error:
    print(error)
    print("I can add int and str !!")
except Exception:
    print("unknow error")
print("this code is execute")
