phones = ["Apple","Samsung","Huawei","Xiomi","Oppo",]
year = ["2020","2021","2022"]
print(phones)
print(len(phones))
print(type(phones))
print(type(year))

phone = list(("Apple","Samsung","Huawei"))
print(phone)

print(phones[1])
print(phones[-1])
print(phones[1:3])
print(phones[:3])
print(phones[3:])
print(phones[-3:-1])

if "Apple" in phones:
  print("Yes, 'Apple' is in the list")

phones[0] = "Redmi"
print(phones)

phones[0:3] = ["Samsung","Apple","Vivo"]
print(phones)

phones.insert(2, "Beeline")
print(phones)

phones.append("Tele2")
print(phones)
operator=["Activ","Beeline"]
phones.extend(operator)
print(phones)

phones.remove("Oppo")
print(phones)

phones.pop(1)
print(phones)

phones.pop()
print(phones)

del phones[0]
print(phones)

phones.clear()
print(phones)

fruit = ["apple", "banana", "cherry"]
for x in fruit:
  print(x)

for i in range(len(fruit)):
  print(fruit[i])

a = 0
while a < len(fruit):
  print(fruit[a])
  any = a + 1

fruit = ["apple", "banana", "cherry", "kiwi", "mango"]
bag =[]

for x in fruit:
  if "b" in x:
    bag.append(x)

print(x)
bag = [x for x in fruit if x != "apple"]
print(bag)

numbers = [x for x in range(10)]

print(numbers)

bag = [x.upper() for x in fruit]
print(bag)

bag = ['banana' for x in fruit]
print(bag)

bag =  [x if x != "banana" else "orange" for x in fruit]
print(bag)

fruit.sort()
print(fruit)

numer = [100, 50, 65, 82, 23]
numer.sort()
print(numer)

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort(reverse = True)
print(fruits)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist.reverse()
print(thislist)

mylist = thislist.copy()
print(mylist)

mylist = list(thislist)
print(mylist)

mylist = thislist[:]
print(mylist)

name = ["Alina", "Bekzat", "Cake"]
old = [13, 12, 13]

person = name + old
print(person)

for x in old:
  name.append(x)

print(name)

name.extend(old)
print(name)