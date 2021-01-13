car = {
  "brand":"Skoda" , 
  "model":"1.8T",
  "year":1979
  }

print(car)

print(car.get("model")) #Use the get method to print the value of the "model" key of the car dictionary.
print(car["year"]) #

car["year"] = 2020 #change value by key
print(car)