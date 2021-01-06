# Create a Parent Class
class Person:
  def __init__(self , fname , lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname , self.lastname)
    print(self.firstname + self.lastname)

kl = Person("KL","CHENG")
kl.printname()

# Create a Child Class
class Student(Person):
  pass

k2 = Student("K2","PP")
k2.printname()

# Add the __init__() Function in the Child Class
# 子類別加入 __init__()後會覆寫,就不再繼承父類別的__init()__
class Programmer(Person):
  def __init__(self , name , age):
    self.name = name
    self.age = age
  
  def printname(self):
    print(self.name)
    print(self.age)

k4 = Programmer("Jassica",35)
k4.printname()

# 保有父類別的__init__(),在子類別的__init__()內呼叫父類別的__init__()
class Programmer(Person):
  def __init__(self , fname  , lname , age , skill):
    Person.__init__(self,fname,lname)
    self.age = age
    self.skill = skill

  def printSkill(self):
    print(self.skill , "is what I use.")

k3 = Programmer("Kevin","Inn",28,"Python")
k3.printSkill()
k3.printname()

# Use the super() Function
# 讓子類別繼承所有方法及屬性 from its parent
class Student(Person):
  def __init__(self,fname , lname):
    super().__init__(fname , lname) #寫法2:Notice:少1個self
    # Person.__init__(self,fname,lname) #寫法1

# Add Properties
class Student(Person):
  def __init__(self,fname,lname):
    super().__init__(fname,lname)
    self.graduationyear = 2019

s = Student("Y","KK")
print(s.graduationyear)

class Student(Person):
  def __init__(self,fname,lname,year):
    super().__init__(fname,lname)
    self.graduationyear = year

b = Student("A","BB",2016)
b.printname() #Parent's printname()方法
print(b.graduationyear)

# Add Methods
# 如果子類別新增的方法與父類別方法同名,則父類別方法會被覆寫
# If you add a method in the child class with the same name as a function in the parent class
# , the inheritance of the parent method will be overridden.
class Student(Person):
  def __init__(self,fname,lname,year):
    super().__init__(fname,lname)
    self.graduationyear = year
  
  def welcome(self):
    print("Welcome", self.firstname , self.lastname, "to the class of" , self.graduationyear)

c = Student("A","B",25)
c.welcome()

