
def prime_fact(n):

    i = 2
    count = 0
    while( i * i <= n):   
        if(bool(n%i) == False):
            count = 0  
            while(n % i == 0):
                count += 1
                n //= i    
            print( i , "^" , count, end=' ')      
        i += 1
    if n>1:
        print( i , "^" , 1, end=' ')      

if __name__ == '__main__':
    prime_fact(50)