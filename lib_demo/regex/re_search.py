import re

r = re.search(r"\d+", "59 abc 78")
print(r)

r = re.search(r"\d+", "abc def xyz")
print(r)

r = re.search(r"\d+", "abc 8787 def")
print(r)
