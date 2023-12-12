# variable assigning
a = [1, 2, 3, 4]
print(id(a))
b = a
print(id(b))
b.append(5)
print(a)
print(b)