import re

f = open("110013.csv",encoding="utf-8")
w = open("110013-new.csv","w",encoding="utf-8")

for line in f:
  x = re.sub("," , "','" ,line ,count=2)
  y = x[:15] + "'" + x[15:]
  # print(y)
  w.write(y)

f.close()
w.close()