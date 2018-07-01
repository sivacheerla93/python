try:
    print("Try")
    v = int("Abc")
    a = 10 / 0
except (ZeroDivisionError, StopIteration) as ex:
    print("Error: ", ex)
except Exception as ex:
    print("Common error: ", ex)
    # prints class of the exception
    print(ex.__class__)
else:
    print("Else")
finally:
    print("Finally")
