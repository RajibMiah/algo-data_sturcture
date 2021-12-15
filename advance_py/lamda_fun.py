
# simple lamda expression

# x = lambda x : x + 10

# x = lambda y , z : y + z

# x = lambda *args : sum(args)

# x = lambda **kwargs: sum(kwargs.values())

# print(x( a = 10 , b = 2 , c = 3 , d = 5 , e = 6))

num = [ 1 , 2 , 3 , 4 , 5]

add = map( lambda x: x + 10 , num )

print(list(add))



