# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Note: This page shows you how to use LISTS as ARRAYS, 
# however, to work with arrays in Python you will have to import a library, like the NumPy library.

cars = ["NISSAN" , "FORD" , "BMW" , "BENZ" , "SKODA"]

def printCars():
  for item in cars:
    print(item)
  print("==========")


x = cars[0]
print(x)

cars[0] = "TOYOTA"
x = cars[0]
print(x)

# Length of an Array
print(len(cars))

# Looping Array elements
for item in cars:
  print(item)
print("=======")

# Adding Array Elements
cars.append("SUSUKI")
printCars()

# Removing Array Elements
cars.pop(1) #移除索引(1)位置的值
printCars()

# Note: The list's remove() method only removes the first occurrence of the specified value.
cars.remove("BENZ") #移除值(BENZ)
printCars()

cars.sort()
printCars()

# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Python沒有內建Array類別,但可用List替代
