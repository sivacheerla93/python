import sys

for p in sys.path:
    print(p)

# as it is list, it is mutable
sys.path.append(".\ds")

print()
print("After appending: ")
for p in sys.path:
    print(p)

print()
print("After removing a path: ")
sys.path.remove(".\ds")
for p in sys.path:
    print(p)
