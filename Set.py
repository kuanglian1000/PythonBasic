fruits = {"apple" , "banana" , "cherry"} #set
more_fruits = ["orange","mango","grapes"] #list

fruits.update(more_fruits) #Notice:加入多個項目，使用UPDATE方法
print(fruits)

fruits.add("orangeA") #加入單個項目,使用add
fruits.add("orangeA") #Set不允許重覆項目 , 此項目未加入
print(fruits)

if "apple" in fruits: #check item in Set
  print("apple in the set.")

fruits.remove("banana") #remove item from Set , not existed raise error(報錯)
print(fruits)

fruits.discard("bibo") #remove item from Set , not existed do nothing.
print(fruits)