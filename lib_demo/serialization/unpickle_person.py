import pickle
from person import Person

f = open("person.dat", "rb")
p = pickle.load(f)
f.close()
print(p)
