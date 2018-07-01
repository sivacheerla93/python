phones = {"Siva": "123456", "Raju": "1234567", "Joe": "026464"}
print(phones)

print()

# getting in sorted order
for name in sorted(phones.keys()):
    print(name, phones[name])
