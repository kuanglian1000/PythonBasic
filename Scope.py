# 變數範圍
# 1.放在 def 裡面,就是 local scope , 只有def內可使用
# 2.放在 def 外面,就是 global scope , def內也可以使用
# 3.若 def 裡外有同名變數 , python 會視為不同變數
# 4.若 def 裡外有同名變數 , 但是 def 裡的變數加上 global , python 則會將兩者視為相同

# Local Scope
def myFun():
  x = 300
  print(x)

myFun()

## Function inside Function
def myFun():
  x = 400
  def myInnerFn():
    print(x)
  myInnerFn()

myFun()

# Global Scope
x = 500
def myFun():
  print(x)

myFun()

# Same Name variable in global scope and local scope
x = 600
def myFun():
  x = 700
  print(x)

myFun()
print(x)

# Global Keyword
def myFun():
  global x
  x = 800

myFun()
print(x)

# Global Keyword (change the value of a global variable inside a function.)
x = 1000
def myFun():
  global x
  x = 1020 #change global var value.

print("before:"+str(x))
myFun()
print("after:"+str(x))
