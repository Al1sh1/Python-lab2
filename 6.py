car = {
  "brand": "Tesla",
  "model": "X",
  "year": 2021
}
print(car)
print(car["brand"])
print(len(car))
print(type(car))

cars = dict(name = "Tesla", model = "X", year = 2022)
print(cars)
x = car.keys()
x = cars.get("model")
print(x)

x = cars.keys()
print(x)
x = car.keys()
car["color"] = "white"
print(x)

x = car.values()
print(x)
car = {
  "brand": "Tesla",
  "model": "X",
  "year": 2021
}
x = car.values()

print(x) 

car["year"] = 2020

print(x) 

x = car.items()

car["year"] = 2025
print(x) 

if "model" in car:
  print("Yes")


car.update({"year": 2020})
car.update({"color": "red"})

car.pop("model")
print(car)

car = {
  "brand": "Tesla",
  "model": "X",
  "year": 2021
}
car.popitem()
print(car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

for x in car:
  print(x)

for x in car:
  print(car[x])

for x, y in car.items():
   print(x, y)

copycar = car.copy()
print(copycar)

copycar = dict(car)
print(copycar)

Shop = {
  "Thing1" : {
    "name" : "milk",
    "expires" : 12.12
  },
  "Thing2" : {
    "name" : "egg",
    "expires" : 13.11
  },
  "Thing3" : {
    "name" : "sugar",
    "expires" : 13.12
  }
}

print(Shop["Thing3"]["name"])

for x, obj in Shop.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])