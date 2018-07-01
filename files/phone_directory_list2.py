phones = dict()

with open(r"D:\Education\git_workspace\python\files\phones2.txt", "rt") as f:
    for line in f.readlines():
        parts = line.split(',')
        if len(parts) < 2:
            continue
        name = parts[0]
        phone = parts[1].strip("\n")

        if name in phones:
            phones[name].add(phone)
        else:
            phones_set = set()
            phones_set.add(phone)
            phones[name] = phones_set
for name, value in sorted(phones.items()):
    print("%-10s" % (name), end='' * 3)
    for p in value:
        print("%-10s" % (p), end='' * 2)
    print()
