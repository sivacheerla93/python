from datetime import *

s = "20180401"
ed = datetime.strptime(s, "%Y%m%d")
print(ed)

s = "2018-04-01 10:20"
ed = datetime.strptime(s, "%Y-%m-%d %H:%M")
print(ed)

cd = datetime.today()
print(cd.strftime("%d/%m/%Y %H:%M"))

ct = datetime.now()
print(ct.strftime("%d/%m/%Y %H:%M"))
