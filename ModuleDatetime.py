# Python Dates
import datetime

x = datetime.datetime.now()
print(x)

# Date Output
print(x.year)
print(x.strftime("%A")) #WeekDay

# Creating Date Objects(must:year,monthd,day ; optional:hour,minute,second,microsecond,tzone)
objDate = datetime.datetime(2021,1,8)
print(objDate)

# The strftime(<format>) Method , string format time(日期格式化)
print(objDate.strftime("%B")) #Month Name

print(objDate.strftime("%U")) #Month Name

