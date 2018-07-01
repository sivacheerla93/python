nums = [10, 11, 20, 21, 30, 31, 40, 41]


def iseven(n):
    return n % 2 == 0


enums = filter(iseven, nums)
for n in enums:
    print(n)

# using lambda
onums = filter(lambda n: n % 2 == 1, nums)
for n in onums:
    print(n)
