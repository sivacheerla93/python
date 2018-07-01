message = input("Enter your message: ")

message = message.upper()
print(message)

if "H" in message:
    print("Letter 'H or h' is present in " + message)
else:
    print("Letter 'H or h' isn't present in " + message)
