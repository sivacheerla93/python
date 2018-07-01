def add(list, item):
    print("The address of list is: ", id(list))
    list.append(item)


names = []
print("The address of names is: ", id(names))
add(names, "Bill")
add(names, "Jeff")
print(names)
