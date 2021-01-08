# 規則運算式 , build-in module <re>

# RegEx Module
import re

# RegEx in Python
txt = "The snow in Taiwan , the sun in ILan , and the rain in Tainan"
s = re.search("^.Taiwan$" , txt)
print(s)

# RegEx Functions
"""
findall => return a list containing all matches (從頭找到尾)
search => return a Match Object if there is a match anywhere in the string (找到第1個就停)
split => return a list where the string has been split at each match (這個看不懂,不知怎麼用)
sub => replace one or many matches with a string (這個好用,被替換的就是找到的,也會列出不吻合的)
"""
tS = "azy bjk cal db"
print(re.split("[a-j]",tS))

# Metacharacters
"""
[] 1組字元 ex."[a-m]"
\ 跳脫字元 ex."\d"
. 所有字元(除了換行字元) ex."he..o"
^ Starts with ex."^hello"
$ Ends with ex."world$"
* Zero or more occurrences "aix*" => aix(match) , ai(match) , ain(match) , aixx(match)
+ One or more occurrences "aix+" => ai(no match) , aix(match) , aixx(match)
{} exactly the specified number of occurrences "al{2}" => all(match) , fall(match) , al(no match) , alll(no match)
| either or "falls|stays" => my cat stays at home => stays(match)
() capture and group
"""
txt = "hello , hebbo , hellK"
print(re.search("he..o",txt))
print(re.findall("he..o",txt))
print(re.split("he..o",txt))
print(re.sub("he..o","2",txt))

# findall() function , The list contains the matches in the order they are found.
# If no matches are found, an empty list is returned:
txt = "The rain in Spain"
x = re.findall("ai" , txt)
print(x)

x = re.findall("taiwan" , txt)
print(x)

# search() function
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, (只有回傳第1個吻合項目)only the first occurrence of the match will be returned
# If no matches are found, the value (None) is returned:
x = re.search("\s" , txt) #\s , 找空白字元
print("The first white-space character is located in position:" , x.start())

x = re.search("taiwan" , txt)
print(x)

# The split() function
# The split() function returns a list where the string has been split at each match
# (最多分割幾次)You can control the number of occurrences by specifying the maxsplit parameter:
x = re.split("\s",txt)
print(x)

x = re.split("\s",txt , maxsplit=1)
print("maxsplit=1 ",x)

x = re.split("\s",txt , maxsplit=2)
print("maxsplit=2 ",x)

# The sub() Function
# The sub() function replaces the matches with the text of your choice
# (只取代幾個)You can control the number of replacements by specifying the count parameter
x = re.sub("\s" , "_" , txt)
print(x)

x = re.sub("\s" , "_" ,txt ,count=2)
print(x)

# Match Object
# (如果沒有找到,則回傳None)Note: If there is no match, the value <None> will be returned, instead of the Match Object.
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
x = re.search("ai",txt)
print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+",txt) # r => 表示為raw string , \b => 開頭 , \w+ => 1個以上的英文字元
print(x.span()) #Match項目的起始及結束位置索引
print(x.string) #被搜尋的原始字串
print(x.group()) #Match項目的值

