print(bool("abc")) # return True
print(bool(0)) # return False

# Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]
print(x)

fruits = ["apple" , "banana"]
if "apple"  in fruits:
  print("Yes , apple is a fruit.")

if 1 and 0:
  print(1)
else:
  print(0)

# 去除字串前後空白值
txt = " Hello World "
print(txt.strip())

# 字串轉大寫
txt = " Hello World "
print(txt.upper())

# 字串轉小寫
txt = " Hello World "
print(txt.lower())

# 字串取代(replace H with K)
txt = " Hello World "
print(txt.replace("H","K"))

# String format()
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple Values
quantity = 3
itemNo = 567
price = 48
myOrder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myOrder.format(quantity , itemNo , price))

# Index Numbers
quantity = 3
itemNo = 567
price = 48
myOrder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myOrder.format(quantity , itemNo , price))

# Index Numbers(相同變數值,使用多次)
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age , name))

# Named Indexes
myOrder = "I have a {carName} , it is a {model}."
print(myOrder.format(carName="Skoda" , model="1.8T"))
