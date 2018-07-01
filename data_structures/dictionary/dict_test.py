# empty dictionary
empty = {}
print(empty)

phones = {"Siva": "123456", "Raju": "1234567"}
print(phones)
print(phones["Raju"])

# adding
phones["Jack"] = "12345"

# updating
phones["Jack"] = "12345678"

print(phones)

# getting only keys
for name in phones.keys():
    print(name)

# KeyError
# print(phones["Steve"])

# returns bool if key existing or not!
print("Steve" in phones)

if "Steve" in phones:
    print(phones["Steve"])
else:
    phones["Steve"] = "1456987"

print(phones)

print()

# getting keys and values
for name in phones.keys():
    print(name, phones[name])

print()

for name, phone in phones.items():
    print(name, phone)

# type # returns 'dict_items'
print(type(phones.items()))

# get() method
print(phones.get("Ramesh"))
print(phones.get("Ramesh", "1090255"))
