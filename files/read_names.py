with open(r"D:\Education\git_workspace\python\files\names.txt", "rt") as f:
    for lineno, name in enumerate(f.readlines(), 1):
        print("{:3} {}".format(lineno, name), end="")
