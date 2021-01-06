# Create a Class
class MyClass():
  x = 5

# Create an object
p1 = MyClass()
print(p1.x)

# __init__() function
# __init__ , 就是 <C# 建構子>
class Person():
  def __init__(self, n , g):
    """
    docstring
    """
    self.name = n
    self.age = g

  # Note: The self parameter is a reference to the current instance of the class
  # , and is used to access variables that belong to the class.
  def myfunc(self):
    print("Hello my name is " + self.name)

p2 = Person("KL",28)

print(p2.name)
print(p2.age)
p2.myfunc()

# The "self" Parameter
# 目前物件參考,用來存取物件變數
# "self" 可以取任意名字,唯一限制是任何函式的第1個參數
class Person:
  def __init__(myObj, na , ag):
    myObj.name = na
    myObj.age = ag
  
  def myFunc(bbc):
    print("My age is " + str(bbc.age))

p3 = Person("kl.cheng",18)
p3.myFunc()

# Modify Object Properties
p3.age = 29
p3.myFunc()

# Delete Object Properties(什麼??)
del p3.age
# p3.myFunc() => 報錯,因為p3的age屬性已被刪除

p4 = Person("KL",20)
p4.myFunc()

# Delete Objects
del p1
del p2
del p3
del p4
# del p5

# The pass Statement
class Person(object):
  """
  docstring
  """
  pass

# 類別定義不能是空的,不過,如果加上 pass 就不會報錯