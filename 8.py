apple = 1
while apple < 6:
  print(apple)
  apple += 1

apple = 1
while apple < 6:
  print(apple)
  if apple == 3:
    break
  apple += 1

apple = 0
while apple < 6:
  apple += 1
  if apple == 3:
    continue
  print(apple)

apple = 1
while apple < 6:
  print(apple)
  apple += 1
else:
  print("apple is less than 6")
