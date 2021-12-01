
def binary_search(number_list , number_to_find , left_index  , right_index  ):
   
    if  right_index >= left_index:
        mid_index = (left_index + right_index) // 2
        right_index = len(number_list) - 1

        if number_list[mid_index] == number_to_find:
            return mid_index + 1

        if number_list[mid_index] > number_to_find:
    
            return binary_search(number_list , number_to_find , left_index , mid_index - 1 )
        else:
            
            return binary_search(number_list , number_to_find , mid_index + 1 , right_index ) 
    return -1

if __name__ == "__main__":
    number_list = [12 , 15, 17 , 19 , 21 ,  24 , 45 , 67]
    number_to_find = 45
    index = binary_search(number_list , number_to_find , left_index = 0 , right_index = 0)
    print('index is ' , index)