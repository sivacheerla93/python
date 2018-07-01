def iseven(n):
    return n % 2 == 0


def ispositive(n):
    return n > 0


if __name__ == "__main__":
    print("Running as script")
else:
    print("Importing module: ", __name__)
