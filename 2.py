x = 5
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = 69
print(x)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

x = 5
x *= 3
print(x)

x = 5
x /= 3
print(x)

x = 5
x %= 3
print(x)

x = 5
x //= 3
print(x)

x = 5
x **= 3
print(x)

x = 5
x &= 3
print(x)


x |= 3
print(x)

x ^= 3
print(x)

x >>= 3
print(x)

x <<= 3
print(x)

print(x := 3)

x = 10
y = 5
print(x == y) #False

x = 10
y = 5
print(x != y) #True

x = 10
y = 5
print(x > y) #True

x = 10
y = 5
print(x < y) #False

x = 10
y = 5
print(x >= y) #True

x = 10
y = 5
print(x <= y) #False

x = 5
print(x > 3 and x < 10)#True

x = 5
print(x > 3 or x < 4)#True

x = 5
print(not(x > 3 and x < 10))#False

x = ["PUBG", "Fortnite"]
y = ["PUBG", "Fortnite"]
z = x
print(x is z)#True
print(x is y)#False
print(x == y)#True

x = ["PUBG", "Fortnite"]
print("Fortnite" in x)#True

x = ["PUBG", "Fortnite"]

print("APEX" not in x) #True

print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~3)
print(3 << 2)
print(8 >> 2)