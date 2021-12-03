
def bubble_sort(arr):

    size = len(arr)
    swapped_flag = False
    
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if(arr[j] > arry[j+1]):
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
                swapped_flag = True
        
        if not swapped_flag:
            break        

if __name__ == '__main__':
    # arry = [52 , 50 ,40 , 5 ,11, 40 ,50 ,0 ]
    # arry = [1 , 2 , 3]
    arry = ["mona" , 'Dhaval' , 'aamir' , 'tine' , 'change']
    bubble_sort(arry)
    print(arry)
