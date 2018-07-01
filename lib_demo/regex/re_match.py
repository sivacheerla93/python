import re

# returns object in the form of string
r = re.match(r"\d", "59")
print(r)

r = re.match(r"\d+", "59 ABC 70 XYZ")
print(r)
