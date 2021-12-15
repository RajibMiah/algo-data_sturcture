from functools import reduce

# simple lamda expression

x = lambda x : x + 10

x = lambda y , z : y + z

x = lambda *args : sum(args)

x = lambda **kwargs: sum(kwargs.values())



# using functools 

num = [ 1 , 2 , 3 , 4 , 5]

add = list(map( lambda x: x + 10 , num ))

filter_num = list(filter(lambda x: x % 2  , num)) # returnd all odd number

cumulative_sum = reduce(lambda x , y : x +  y , range(1 , 10))

def count(x):
    y = x + 10
    return (lambda x : x + 10) (y)

print("add number" ,add )
print('filter numbers ', filter_num)
print('cumulative sum' , cumulative_sum)


print(count(10))    


