# normal fuction
def isEven(n):
    return True if n % 2 == 0 else False


# lambda function
isOdd = lambda n: n % 2 == 1

# lambda function with multiple arguments
add = lambda a, b: a + b

print(isEven(10))
print(isEven(15))

print(isOdd(10))
print(isOdd(15))

print("Addition of 10 & 20 is: ", add(10, 20))
