cars = ("Toyota", "Tesla", "Merz","Zeekr","Nissan")
print(cars)
print(len(cars))
print(type(cars))
print(cars[1])
print(cars[-1])
print(cars[0:2])
print(cars[:2])
print(cars[2:])
print(cars[-2:-1])

if "Toyota" in cars:
    print("Yes")

newcars= list(cars)
newcars[1]="bmw"
cars=tuple(newcars)
print(cars)

y = list(cars)
y.append("Audi")
cars = tuple(y)
print(cars)

y = ("Hummer",)
cars += y
print(cars)

cars = ("Toyota", "Tesla", "Merz","Zeekr","Nissan")
y = list(cars)
y.remove("Tesla")
cars = tuple(y)

cars = ("Toyota", "Tesla", "Merz")

(green, yellow, red) = cars

print(green)
print(yellow)
print(red)

(green, yellow, *red) = cars

print(green)
print(yellow)
print(red)


(green, *yellow, red) = cars

print(green)
print(yellow)
print(red)
cars = ("Toyota", "Tesla", "Merz","Zeekr","Nissan")
for x in cars:
  print(x)
cars = ("Toyota", "Tesla", "Merz","Zeekr","Nissan")
for i in range(len(cars)):
  print(cars[i])
cars = ("Toyota", "Tesla", "Merz","Zeekr","Nissan")
i = 0
while i < len(cars):
  print(cars[i])
  i = i + 1

name = ("Ali", "Baglan" , "Didar")
old = (21, 22, 23)

man = name + old
print(man)

names = name * 2

print(names)

cars = ("Toyota", "Tesla", "Toyota","Zeekr","Toyota")
x = cars.count("Toyota")
print(x)
x = cars.index("Toyota")
print(x)