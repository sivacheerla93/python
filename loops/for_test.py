message = "Hello Python"
for i in message:
    print(i, end=' ')

print('\n')
print(len(message))
print(len(message) - 1)

for idx, val in enumerate(message, 100):
    print("Index is ", idx, "value is ", val)
for i in range(6, len(message)):
    print(message[i])

for i in range(1, 10):
    print(i, end=' ')

print()

for i in range(30, 1, -2):
    print(i, end=' ')
