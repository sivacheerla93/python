import pickle
from person import Person

f = open("person.dat", "wb")
p1 = Person("Siva", "sivacheerla@live.com")
pickle.dump(p1, f)
print("Dumped to file!")
f.close()
