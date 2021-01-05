# Lambda function is a small anonymous function
# Lambda function can take any number of arguments(可以有多個參數) ,
#  but can only have one expression.(只能有1個表達式)
# Syntax => lambda arguments : expression

x = lambda a: a + 10
print(x(20))

x = lambda a , b: a * b
print(x(7,20))

x = lambda a , b, c : a+b+c
print(x(1,2,3))

def myfunc(n):
  return lambda a: a * n

mydouble = myfunc(2)
print(mydouble(11))

mytrible = myfunc(3)
print(mytrible(11))