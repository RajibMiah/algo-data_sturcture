import sys

#infinit_sequeance

def infinit_sequance():
    result = 1
    while True:
        yield result
        result *= 5


#lazy excecution
def generator(n):
    for x in range(n):
        yield x ** 3

values = generator(1000)

# for x  in values:
#     print(x)
print("getting size of the stack function",sys.getsizeof(values))

print(next(infinit_sequance()))
print(next(infinit_sequance()))
print(next(infinit_sequance()))
print(next(infinit_sequance()))
print(next(infinit_sequance()))
print(next(infinit_sequance()))

# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))