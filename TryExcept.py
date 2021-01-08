# Exception Handling
try:
  print(x)
except :
  print("An exception occurred..")

# Many Exceptions
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong.")

# Else : 沒有異常發生時,會執行ELSE
try:
  print("hello")
except:
  print("Something else went wrong.")
else:
  print("Nothing went wrong.")

# Finally : 無論異常發生與否,都會執行Finally
try:
  f = open("demofile.txt")
  f.write("Hello Everyone.")
except:
  print("Error: File Writing.")
# finally:
#   f.close() #這裡一樣會出錯.

# Raise an exception
# To throw (or raise) an exception, use the <raise> keyword.
# x = -1
# if x < 0:
#   raise Exception("Error : x is small then zero.")

x = "hello"
print(type(x))

if not type(x) is int:
  raise TypeError("Only integer allowed.")

