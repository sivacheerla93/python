def change(n):
    print(id(n))  # 1666107760 as v = 10 before assigining n = 0
    n = 0
    print(id(n))  # 1666107440 as n = 0


v = 10
print("The address of v is: ", id(v))  # 1666107760
change(v)
