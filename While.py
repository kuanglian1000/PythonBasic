i = 1
while i < 6: #符合條件 , 停止LOOP
  print(i)
  i += 1

i = 1
while i < 6:
  if i == 3:
    break #break , 停止LOOP
  else:
    print(i)
  i+=1

i = 0
while i < 6 :
  i += 1
  if i == 3:
    continue #continue , 直接跳到下個迴圈
  print(i)

# Print a message once the condition is false.(這種寫法沒看過)
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less then 6")