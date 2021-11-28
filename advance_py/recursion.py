
#problem calculate the  sum of  list  ===> x = [[1,2] ,[[3] 4, [5 , 6]] ,[7,[8]]]

def addition(array):
    total = 0 
    for x in array:
        if type(x) != list:
              total +=  x
        else:
            total += addition(x) # 3 + 3 + 4 + 11 + 15 = 36
    return total
   

if __name__ == "__main__":
    print(addition([[1,2] ,[[3], 4, [5 , 6]] ,[7,[8]]]))
