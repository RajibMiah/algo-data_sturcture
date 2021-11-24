import time

#practical example #2 timing function
def timed(function):

    def wrapper(*args , **kwargs):
        before = time.time()
        reutrn_value = function(*args , *kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after - before} seconds to execute!!")
        return reutrn_value
    return wrapper    

#practical example #1 logging
def logged(function):
    def wrapper(*args , **kwargs):
        return_fun = function(*args , **kwargs)
        with open('logfile.txt' , 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {return_fun}")
            f.write(f"{fname} returned value {return_fun}")
        return return_fun    

    return wrapper 

def wrapperFunction(function):

    def wrapper(*args , **kwargs):
        retrun_value = function(*args , **kwargs)
        print("I am decorating the function")
        return retrun_value
        
    return wrapper

@timed
def myfunction(x):
    result = 1
    for i in range(1,x):
        result *= i
    return result


@wrapperFunction
def hello(person):
    print('execuite this line first ')
    print(f"hello world!!! to person {person}")  


if __name__ == '__main__'

myfunction()
# print(add(10, 30))
# hello('mike')