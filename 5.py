color = {"red", "blue", "yellow"}
print(color)

color = {"red", "blue", "yellow",1,2,True}
print(color)

color = {"red", "blue", "yellow","pink","black"}
print(len(color))

color = {"red", "blue", "yellow","pink","black"}
print(type(color))

color = {"red", "blue", "yellow","pink","black"}
for x in color:
  print(x)

print("blue" in color)

print("yellow" not in color)

color = {"red", "blue", "yellow","pink","black"}
color.add("orange")
print(color)

newcolor = {"gray","dark"}
color.update(newcolor)
print(color)

color = {"red", "blue", "yellow","pink","black"}
color.remove("blue")
print(color)
color = {"red", "blue", "yellow","pink","black"}
color.discard("yellow")
print(color)

color.pop()
print(color)
color = {"red", "blue", "yellow","pink","black"}
color.clear()
print(color)

for x in color:
  print(x)

color = {"red", "blue", "yellow"}
number = {1, 2, 3}

numer = color.union(number)
print(numer)

color = {"red", "blue", "yellow"}
number = {1, 2, 3}

numer = color | number
print(numer)

color.update(number)
print(number)

color = {"red", "Orange", "yellow"}
thing = {"Toy","Car","Orange"}
tot = color.intersection(thing)
print(tot)

tot = color & thing
print(tot)

color.intersection_update(thing)
print(color)

color = {"red", "Orange", "yellow"}
thing = {"Toy","Car","Orange"}
tot = color.difference(thing)
print(tot)

color = {"red", "Orange", "yellow"}
thing = {"Toy","Car","Orange"}
tot = color-thing
print(tot)

color = {"red", "Orange", "yellow"}
thing = {"Toy","Car","Orange"}
color.difference_update(thing)
print(color)

color = {"red", "Orange", "yellow"}
thing = {"Toy","Car","Orange"}
tot = color.symmetric_difference(thing)
print(tot)

color = {"red", "Orange", "yellow"}
thing = {"Toy","Car","Orange"}
tot = color^thing
print(tot)
