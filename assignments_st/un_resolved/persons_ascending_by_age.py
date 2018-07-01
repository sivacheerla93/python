from datetime import *
import operator

data = dict()

with open(r"D:\Education\git_workspace\python\lib_demo\date_time\persons.txt") as f:
    for line in f.readlines():
        parts = line.split(',')
        if len(parts) < 2:
            continue
        data[parts[0]] = parts[1].strip("\n")

today = datetime.today().strftime("%Y")
print(today)

for name, dob in data.items():
    # age1 = date(int(age[0:4]), int(age[5:7]), int(age[8:]))
    age = str(int(today) - int(dob[0:4]))
    print(name, dob, age)
