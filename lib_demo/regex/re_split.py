import re

m = re.split("[a-z]+", "123abc456def")
print(m)

m = re.split("[a-z]+", "123abc456def789hbkfhbk", maxsplit=2)
print(m)

m = re.split("[a-z]+", "123ABC456def789hbDDFfhbk", maxsplit=2, flags=re.IGNORECASE)
print(m)
