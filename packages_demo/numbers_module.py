def even(target):
    for i in range(2, target):
        if i % 2 == 0:
            print(i)


def odd(target):
    for i in range(1, target):
        if i % 2 == 1:
            print(i)


def positive(num):
    if num > 0:
        print("Positive number!")
    else:
        print("Zero (or) Negative number!")
