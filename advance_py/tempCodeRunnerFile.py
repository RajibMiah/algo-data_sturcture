import time
def timed(function):

    def wrapper(*args , **kwargs):
        before = time.time()
        return_value = function(*args , **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute!")
        return return_value

@timed
def myfunction(x):
    result = 1
    for i in range(1 , x):
        result *= i
    return result


myfunction(500000)