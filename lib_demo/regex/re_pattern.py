import re

p = re.compile(r"\d+")

m = re.search(p, "abc 123 def 456 xyz 789")
print(m)
print(m.group(), m.start(), m.end(), m.span())

m = re.search(r"([a-z]+) (.+)", "abc 112 343")
print(m.group(1), m.start(1), m.end(1), m.span(1))
print(m.group(2), m.start(2), m.end(2), m.span(2))

m = re.search(r"([a-z]+) (\d+)", "abc 113 343 xyz")
print(m.group(1), m.start(1), m.end(1), m.span(1))
print(m.group(2), m.start(2), m.end(2), m.span(2))
print(m.group())
print(m.group(1, 2))
print(m.groupdict())
