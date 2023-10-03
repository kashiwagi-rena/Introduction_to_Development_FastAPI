class Animal:
  height = 30

animal1 = Animal()
animal2 = Animal()
print(animal1.height)
print(animal2.height)

animal1.height = 10
print(animal1.height)
print(animal2.height)

print(animal1.__dict__)
print(animal2.__dict__)