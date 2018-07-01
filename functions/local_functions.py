def f1():
    def f2():
        print("From f2()")

    print("From f1()")
    f2()


f1()
