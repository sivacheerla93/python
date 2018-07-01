import sys
from math import sqrt

print(type(sys.argv))
num = int(sys.argv[1])

for i in range(2, int(sqrt(num) + 1)):
    if num % i == 0:
        print("Not a prime number!")
        break
else:
    print("Prime number!")
