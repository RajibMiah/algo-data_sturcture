

#inverse pyramid
def inverse_payramid(n):
    k =  2*n 
    for i in range(n , -1, -1):
        for s in range( k , 0 , -1 ):
            print(end=' ')   
        k = k + 1 
        for j in range(0 , i):
            print('* ' , end='')
        print('\r')    


#pyramid
def payramid_pattern(n):
    k = 2*n 
    for i in range(0 , n):
        for s in range(0 , k):
            print(end=' ')
        k = k - 1    
        for j in range(0 ,i):
            print('* ' , end= '')
        print('\r')       

if __name__ == '__main__':
    payramid_pattern(10)
    inverse_payramid(10)

