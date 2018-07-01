# open file for writing in text mode
try:
    with open(r"D:\Education\git_workspace\python\files\names.txt", "wt") as f:
        names = ["Python", "C#", "Java", "JavaScript", "C++"]
        for name in sorted(names):
            f.write(name + "\n")
        print("Write successful!")
except Exception as ex:
    print("Error: ", ex)
