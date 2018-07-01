langs = set()
langs2 = set()

print(langs)

langs.add("Java")
langs.add("Python")
langs2.add("C#")
langs2.add("Python")
print(langs)
print(langs2)
print(langs2.isdisjoint({"C#", "C"}))  # prints true if there are no common elements
