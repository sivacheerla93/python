import re

r = re.search(r"\d+", "abc 8787 def")
if r:
    print(r.group())
else:
    print("Not found!")

r = re.search(r"\d+", "abc xyz def")
if r:
    print(r.group())
else:
    print("Not found!")
