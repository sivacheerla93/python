import sys
from math import sqrt

# print(type(sys.argv))
if len(sys.argv) == 1:
    print("Usage: python prime_cmd_multple_args.py 21 22 23")
    sys.exit(0)
for i in range(1, len(sys.argv)):
    num = int(sys.argv[i])

    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            print(num, "Not a prime number!")
            break
    else:
        print(num, "Prime number!")
