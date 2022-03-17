
def isPalRec(str , l , r):

    if l == r:
        return True
    if (str[l] != str[r]):
        return False

    if (l < r + 1 ):
        res =  isPalRec(str , l + 1 , r - 1)
        return res
    return True            

def isPalindrom(str):
    n = len(str)

    if (n == 0):
        return True

    return isPalRec(str , 0 , n - 1)    


if __name__ == '__main__':
    s = 'geg'
    if(isPalindrom(s)):
        print('yes')
    else:
        print('No')    