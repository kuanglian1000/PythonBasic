# File Handling
# open(filename , mode)
# mode :
#   r => Read , 開啟,檔案不存在報錯
#   a => Append , 附加資料,檔案不存在則新增
#   w => Write , 寫入資料,檔案不存在則新增
#   x => Create , 新增檔案,檔案存在報錯

# 另外,mode還能指定是 binary or text mode
#   b => binary , 圖片或檔案 , 須特別指定
#   t => text , 字串或字元 , 預設值(可不指定)

import os.path

filePath = "demofile.txt"
if not os.path.isfile(filePath):
  f = open("demofile.txt" , "x") #新增檔案
  print("Create new file..")
else:
  f = open("demofile.txt" , "rt") #以文字模式讀檔
  print("Read Existed file..")

# Open a File on the Server
print(f.read()) #1次全部讀出來

# Read Only Parts of the File(讀取中文,指定UTF-8字碼讀取,而非預設本機的CP950)
f = open("D:\\tmp\\log\\ePolicyProcess\\demofile5678.txt","r" , encoding="utf-8")
print(f.read(5)) #先讀,前5個字元
print(f.read(500)) #接續讀,後面500個字元

f = open("demofile.txt" , "r")
print(f.readline())
print(f.readline())
print(f.readline())

f = open("demofile.txt","r")
for line in f:
  print(line)
f.close()

# Close Files
f = open("demofile2.txt","r")
for line in f:
  print(f.readline())
f.close()

# Writing to an Existing File(append)
f = open("demofile2.txt","a") #append
f.write("Now the file has more content!")
f.close()

f = open("demofile2.txt","r")
print(f.read())

# Writing to an Existing File(Override)
f = open("demofile3.txt","w") #write file , override the entire file.
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile3.txt","r")
print(f.read())


# Check if File exist & Delete a File
import os
if os.path.exists("myFile.txt"):
  os.remove("myFile.txt")
else:
  print("<File does not exist>")
  
# Create a New File
f = open("myFile.txt","x") #執行第二次會報錯,因為檔案已存在

os.mkdir("myfolder") #Create Folder
f = open("myfolder\myFile1.txt","x")
f.close()

#Note:Python只允許刪除空資料夾
os.rmdir("myfolder") #Delete Folder => error： OSError: [WinError 145] 目錄不是空的。: 'myfolder'
