fruits = ["apple" , "banana" , "cherry"]
for x in fruits:
  print(x)

for x in fruits:
  if x == "banana":
    continue
  print(x)

# Use the <range> function to loop through a code set 6 times.
for x in range(6):
  print(x) # 0,1,2,3,4,5

# Exit the loop when x is "banana"
for x in fruits:
  if x == "banana":
    break
  print(x)