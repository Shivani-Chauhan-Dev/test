x = 20
y = 20
z = 20
print(id(x))

print(id(y))

print(id(z))

print(x is y)
print(y is z)
print(z is x)

x = 100
y = 257
z = 100
print(id(x))
print(id(y))
print(id(z))

z = 257
print(id(z))

print(x is y)
print(x is z)
print(y is z)
print(z is x)

x = 258
z = 258
print(id(x))
print(id(z))

print(x is z)

