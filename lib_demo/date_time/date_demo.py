from datetime import *

sd = date(2018, 1, 1)
print(sd)

cd = date.today()
print(cd)

# timedelta
td = cd - sd
print(td.days, td.seconds)

# adding days using timedelta
nd = cd + timedelta(days=10)
print(nd)
