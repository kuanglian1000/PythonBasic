# Single Argument
def my_function(fname):
  print(fname + '...')

my_function('Hello')

# Arbitrary Arguments
def my_function(*args):
  print("Arbitrary Arguments," + str(args[2]))

my_function('台中','花蓮','台北')

# Keyword Arguments(kwargs)
def my_function(child1 , child2 , child3):
  print("The youngest child is " + child3)

my_function(child1="Jason" , child2="Kevin"  , child3="Susan")

# Arbitrary Keyword Arguments , **kwargs
# 可變的指名參數 , 它會收到 1個Dictionary , 而且可以直接用 Key取值
def my_function(**kwargs):
  print("His last name is " + kwargs["lname"])

my_function(kname="1" , lname="2")

# Default Paramter Value
def my_function(country="Taiwan"):
  print("I am from " + country)

my_function("Sweden")
my_function("Japan")
my_function()
my_function("UK")

# Passing a List as an Argument
def my_function(food):
  for f in food:
    print(f)

fruits = ["apple" , "banana" , "cherry" , "watermelon"]

my_function(fruits)

# Return Values
def my_function(x):
  return x * 5

print(my_function(6))
print(my_function(8))

# The pass Statement
def my_function():
  """
  Do nothing.
  """
  pass

my_function()

# Magic , python的函式寫上面 , 下面可以直接呼叫
# my_function('test')

# my_function('World')


