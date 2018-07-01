from datetime import *

t1 = time(hour=10, minute=20, second=30)
print(t1)

t2 = time()
print(t2)

print(type(t2))

ct = datetime.now().time().strftime("%H:%M:%S")
print(ct)
ct1 = datetime.now() + timedelta(0, 300)  # (Days, Seconds)
print(ct1.strftime("%H:%M:%S"))
