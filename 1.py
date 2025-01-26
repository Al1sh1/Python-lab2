print(150 > 9) #1
print(10 == 9) #0
print(1 < 23)  #0


a=120
b=33
if b<a:
    print("A is bigger")
else:
    print("a is NOT bigger")

print(bool("Hotline")) #1
print(bool("1991")) #1

x="Miami"
y=51

print(bool(x)) #1
print(bool(y)) #1

print(bool("Jacket")) #1
print(bool(51)) #1
print(bool(["S", "C", "A"])) #1

print(bool(False)) #0
print(bool(None)) #0
print(bool(0)) #0
print(bool("")) #0
print(bool(())) #0
print(bool([])) #0
print(bool({})) #0

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #0

def correctfunction() :
  return True

print(correctfunction()) #true

def Function() :
  return True

if Function():
  print("YES!")
else:
  print("NO!") #YES!

x = 200
print(isinstance(x, int))
