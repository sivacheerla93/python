import re

phones = dict()
with open(r"D:\Education\git_workspace\python\files\phones.txt", "rt") as f:
    for line in f.readlines():
        parts = line.split(',')
        if len(parts) < 2:
            continue

        name = parts[0]
        mobile = parts[1].strip("\n")

        if not re.fullmatch(r"[a-zA-Z]+", name):
            continue
        if not re.fullmatch(r"\d{10}", mobile):
            continue

        phones[parts[0]] = parts[1].strip('\n')
for name, value in sorted(phones.items()):
    print(name, value)
