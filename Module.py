# Use a Module
import myModule

# 使用Module內的Function,要加上Module Name
myModule.greeting("KL.JOJO")

# Variable in Module
age = myModule.person1["age"]
print(age)

# Naming a Module(ReNameing a Module)
import myModule as mx
a = mx.person1["age"]
print(a)

# Import Built-in Modules
import platform
x = platform.system()
print(x)

# Use the dir() Function , 可以列出 Module內的函式或變數名稱
n = dir(myModule)
print(n)

p = dir(platform)
print(p)

# Import From Module , 只引用 Module 內想要的項目(函式或變數均可)
# Notice:利用from <moduleName> import <moduleFn|moduleVar>後,
#  再使用時,就毋須加上<moduleName>. Ex. (O)person1 , (X)myModule.person1
from myModule import person1
print(person1["name"])

