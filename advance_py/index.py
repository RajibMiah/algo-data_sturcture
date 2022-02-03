



# n = 10000000000
# count = 0
# print('is divived' , 18 % 4 == 0)
# for i in range(2 , n):
    
#     if( n % i == 0):
#         # print(i)
#         count += 1

# print(count)





# import random
# n = 20  

# to_be_guessed = int(n * random.random()) + 1

# guess = 0

# while guess != to_be_guessed:
#     guess = int(input('New number: '))
#     if guess > 0:
#         if guess > to_be_guessed:
#             print('number too large')
#         elif guess < to_be_guessed:
#             print('Number too small')
#     else:
#         print('sorry that youre giving up!')
#         break

# else:
#     print('Congratulation . You made it!!!')                



# from collections import namedtuple
# a = namedtuple('courses' , 'name , technology')
# s = a('data science' , 'python')
# print(s)










# fruits = {"name":'rajib'}

# i = 0

# while i < len(fruits):
#   print(fruits[i])
#   i += 1

# if __name__ == '__main__':
#     pass  

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