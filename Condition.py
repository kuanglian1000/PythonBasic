
a = 50
b = 10
if a > b : # >
  print("a > b")

if a != b: # !=
  print("a != b")

if a == b : # ==
  print("Yes")
else:
  print("No")

if a == b :
  print("1")
elif a > b: #elif
  print("2")
else:
  print("3")

a = b = c = d = 5
if a == b and c == d: # and
  print("Test AND")

a = 5
b = 6
c = d = 7
if a == b or c == d: # or
  print("Test OR")

# short hand syntax function
if 5 > 2:
  print("Five is greater than two!")

if 5 > 2: print("(Short)Five is greater than two!")
# if (5 > 2) print("(Short)Five is greater than two!") #Error

# 三元運算式(c#)
# (5 > 2) ? print("Yes") : print("No")

# 三元運算式(python)
print("Yes") if (5>2) else print("No") #這樣的寫法真的很奇怪...
print("Yes") if 5 > 2 else print("No") #這樣的寫法真的很奇怪...