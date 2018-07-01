import re

m = re.fullmatch(r"\d+", "abc 345 xyz 123")
print(m)

m = re.fullmatch(r"\d+", "345123")
print(m.group())

valid_mobile = re.fullmatch(r"\d{10}", "1234567890")
print(valid_mobile.group())
