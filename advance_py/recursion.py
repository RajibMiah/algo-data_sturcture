
#problem sum of all list  ===> x = [[1,2] ,[[3] 4, [5 , 6]] ,[7,[8]]]

def addition(array):
    total = 0
    for x in array:
        if type(x) != list:
            total += x
        else:
            total += addition(x)
    return total
   

if __name__ == "__main__":
    print(addition([[1,2] ,[[3], 4, [5 , 6]] ,[7,[8]]]))