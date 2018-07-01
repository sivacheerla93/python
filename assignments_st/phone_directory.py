phones = {}

while True:
    name = input("Enter name: ")
    if name == "end":
        break

    mobile = input("Enter mobile number: ")

    if name in phones:
        phones[name].add(mobile)  # adds new mobile no to existing set
    else:
        phones[name] = {mobile}  # adds a new entry with name and set

    for name, numbers in sorted(phones.items()):
        print(name, numbers)

print(phones)
