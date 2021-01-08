# Python Iterators

# Technically, in Python, an iterator is an object which implements the iterator protocol, 
# which consist of the methods __iter__() and __next__().

# Iterator vs Iterable
# Lists , tuples , dictionaries , sets , string 都是 Iterable物件
# 可利用 iter() 函式來取得 Iterator
# 有趣的是, Iterator從頭到尾只跑1次 , 當跑到最後1個值 
# , 再執行 "next(iterator)" or "for x in iterator" 都不會有結果產出

myTuple = ("apple" , "banana" , "cherry")
for target_list in myTuple:
  print("1" + target_list)

myIterator = iter(myTuple)
print(next(myIterator)) #print apple
# print(next(myIterator))
# print(next(myIterator))

for x in myTuple:
  print("2" + x) #print banana & cherry

myStr = "banananananaK"
for s in myStr:
  print("3" + s)

iteStr = iter(myStr)
for s in iteStr:
  print("4" + s)
# print("5" + next(iteStr)) #報錯,因為iteStr已經跑到最後1個了(END)

# Looping Through an Iterator
# The for loop actually creates an iterator object 
# and executes the next() method for each loop.
myFavoriteFruits = ["banana","orange","apple","kiwi"]
for f in myFavoriteFruits:
  print(f)


# Create an Iterator Class
# 新增自訂Iterator類別,要實作 __iter()__ & __next()__ 方法
# __iter()__ , 作初始化 , 須回傳 iterator 物件本身
# __next()__ , 作處理後 , 須回傳 sequence的下個值

class MyNumbers:
  def __iter__(self):
    self.ini = 0
    return self

  def __next__(self):
    self.ini += 1
    return self.ini


myObj = MyNumbers()
myIteObj = iter(myObj)

print(next(myIteObj))
print(next(myIteObj))
print(next(myIteObj))
print(next(myIteObj))

# Create an Iterator Class with StopIteration(結束條件)
# 如果沒有 Iterator 沒有加上 StopIteration(結束條件) , 會一直執行下去

class IteratorHasStop():
  def __iter__(self):
    self.i = 1
    return self
  
  def __next__(self):
    if self.i < 20:
      self.i += 1
      return self.i
    else:
      raise StopIteration

myClass1 = IteratorHasStop()
for t in myClass1:
  print(t)

