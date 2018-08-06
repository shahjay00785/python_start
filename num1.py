n1 = input("num 1->")  # 4
n2 = input("num 2->")  # 6
n3 = input("num 3->")  # 2

if n1 < n2 and n1 < n3:
    print("n1 small")
elif n2 < n3 and n2 < n1:
    print("n2")
else:
    print("n3 is small")
