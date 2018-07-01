person = ("Siva", ["Python", "JavaScript"])
print(person)
print(person[1])
person[1].append("Angular")  # as it is immutable, if it contains list, the list can become mutable not set
print(person)
print(person[0])
print(person[1])
