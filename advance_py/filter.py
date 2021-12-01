
# Filter types

class Animal:
    def __init__(self , name) -> None:
        self.name = name

class Dog(Animal):
    def __init__(self , name) -> None:
        super().__init__(name)

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

animals = []

for x in range(10):
    name = 'Animal ' + str(x)
    if(x % 2) == 0:
        animals.append(Cat(name))
    else:
        animals.append(Dog(name))  

# for a in animals:
#     print(f'Animal:{a.name}')

def dogfilter(value):
    return isinstance(value , Cat)

def catfilter(value):
    return isinstance(value , Dog)

for d in (list(filter(dogfilter , animals))):
    print(f'Dog:{d.name}')

for d in (list(filter(catfilter , animals))):
    print(f'Cat:{d.name}')

# import random

# v = []

# for x in range(10):
#     v.append(random.randrange(100))

# def lower(value):
#     if value < 50:
#         return True
#     return False    

# f = list(filter(lower , v))

# print(f)

if __name__ == '__main__':
    pass