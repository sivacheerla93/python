unique_names = set()
duplicate_names = set()

while True:
    name = input("Enter name here('end' to stop): ")
    if name == "end":
        break
    if name in unique_names:
        duplicate_names.add(name)
    else:
        unique_names.add(name)

print()

print("Unique names are: ")
for i in unique_names:
    print(i)

print()

print("Duplicate names are: ")
for i in duplicate_names:
    print(i)
