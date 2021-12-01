
fruits = {"name":'rajib'}

i = 0

while i < len(fruits):
  print(fruits[i])
  i += 1

if __name__ == '__main__':
    pass  
#type hinting

# def myfunction(myparameter:int)->str:
#     return myparameter + 10

# def myfunction(param:int) -> int:
#     return param + 10

# def otherfunction(otherparameter: str):
#     print(otherparameter)

# otherfunction(myfunction(10))

# decorators

# def mydecorator(function):
    
#     def wrapper( *args , **kwargs):
#         print('I am decorating your function! ')
#         return function( *args , **kwargs)
#     return wrapper    


# decorator practical exam #2 - timing
# import time
# def timed(function):

#     def wrapper(*args , **kwargs):
#         before = time.time()
#         return_value = function(*args , **kwargs)
#         after = time.time()
#         fname = function.__name__
#         print(f"{fname} took {after-before} seconds to execute!")
#         return return_value
#     return wrapper
# @timed
# def myfunction(x):
#     result = 1
#     for i in range(1 , x):
#         result *= i
#     return result


# myfunction(90000)

# practical example #1 - logging

# def logged(function):

#     def wrapper( *args , **kwargs):
#         pass



# @mydecorator
# def hello_worrd(person):
#     print(f"hello {person}!")

# hello_worrd("rajib")