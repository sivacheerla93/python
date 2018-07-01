fruits = ['orange', 'apple', 'grape', 'mango', 'apple']

print(fruits)

print(fruits.count('apple'))

fruits.append('banana')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.index('apple'))

fruits.insert(1, 'mango')
print(fruits)

fruits.pop()
print(fruits)

# it can be iterable
new_fruits = []
for fruit in fruits:
    new_fruits.append(fruit.upper())
print(new_fruits)

print(len(fruits))

fruits.reverse()
print(fruits)
