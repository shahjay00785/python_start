# for loop with list and break and countinue


'''student_names = ["james", "katarian", "Mark", "jessica",
                 "bort", "Frank"]

for name in student_names:
    if name == "Mark":
        print("Found Him "+name)
    print("currently Testing "+name)'''

"""
student_names = ["james", "katarian", "Mark", "jessica",
                 "bort", "Frank"]


for name in student_names:
    if name == "Mark":
        print("Found Him "+name)
        break
    print("currently Testing "+name)
"""

student_names = ["james", "katarian", "Mark", "jessica",
                 "bort", "Frank"]

for name in student_names:
    if name == "Mark":
        continue
        print("Found Him "+name)
    print("currently Testing "+name)
