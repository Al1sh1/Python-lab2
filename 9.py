cars = ("Toyota", "Tesla", "Merz","Zeekr","Nissan")
for x in cars:
  print(x)

for x in "cars":
  print(x) 

for x in cars:
  print(x)
  if x == "Merz":
    break

for x in cars:
  if x == "Merz":
    break
  print(x)

for x in cars:
  if x == "Merz":
    continue
  print(x)

for x in range(7):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(0, 60, 5):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finish!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finish!")

name = ("Ali", "Baglan" , "Didar")
old = (21, 22, 23)

for x in name:
  for y in old:
    print(x, y)