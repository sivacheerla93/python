a = "Siva Cheerla"

print(len(a))

for i in range(len(a)):
    print(a[i], end='')

print()

for ch in a:
    print(ch, end='')

print()

for ch in reversed(a):
    print(ch, end='')

print()

for ch in sorted(a):
    print(ch, end=' ')

print()
print(a.find('v'))
print(a.find('a', 5))  # skips 1st 5 positions
print(a.isalpha())
print(a.split())
print(a.split('v'))

# Slicing
print(a[1:3])
print(a[3:])
print(a[:3])
print(a[-2:])
print(a[:-2])
print(a[1:4:1])
print(a[1:4:2])
print(a[::2])
print(a[::-1])
print(a[1:3:-1])
print(a[5:1:-1])
print(a[5:3:-1])

print(a.count('e'))
