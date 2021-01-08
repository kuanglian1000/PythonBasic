# Build-in package
import json

# Parse JSON - JSON String to Python Dic
x = '{"name":"KL","age":30,"city":"ILan"}' # Json string
y = json.loads(x) # parse Json string to Python dic
print(y["city"]) # the result is a Python dictionary

# Parse JSON - Python Dic to JSON String
x = {
  "name":"Cherry",
  "age":28,
  "city":"Kaohsiung"
} # Python Dic Object
y = json.dumps(x) # convert into JSON
print(y) # the result is JSON String

# Belowed Python Objests Eable Convert to JSON
"""
dic{} => Object
, list[] => Array
, tuple() => Array
, string  => String
, int  => Number
, float => Number
, True  => true
, False => false
, None => null
"""
print(json.dumps({"math":12,"eng":50,"chi":70}))
print(json.dumps(["sky","sea","land"]))
print(json.dumps(("car","bus","bike","train")))
print(json.dumps("Friday"))
print(json.dumps(42))
print(json.dumps(1.25))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

realData = {
  "name":"KL",
  "age":30,
  "married":True,
  "divorced":False,
  "children":("Hana","Leo"),
  "pets":None,
  "cars":[
    {"model":"YAMAHA 125","tag":608},
    {"model":"SKODA 1.8T","tag":1021}
  ]
}

print(json.dumps(realData))

# Format the Result(增加縮排,讓JSON easier to read the result)
print(json.dumps(realData , indent=2))
# default separator( , : ) => new separator( . = )
print(json.dumps(realData , indent=2 , separators=("."," = ")))

# Order the Result
print(json.dumps(realData , indent=2 , sort_keys=True))