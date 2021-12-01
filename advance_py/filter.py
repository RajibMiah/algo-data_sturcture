
import random

v = []

for x in range(10):
    v.append(random.randrange(100))

def lower(value):
    if value < 50:
        return True
    return False    

f = list(filter(lower , v))

print(f)

if __name__ == '__main__':
    pass