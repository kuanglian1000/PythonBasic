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
