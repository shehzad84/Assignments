#Using third Variable
a=10
b=20
test = a
a = b
b = test
print(a)
print(b)

# without using third variable
a = a + b
b = a - b
a = a - b

print(a)
print(b)
