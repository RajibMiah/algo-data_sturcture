# def factorial(n):
#     print(n) # 5 4 3 2 1
#     if n == 1:
#        return n

#     return n * factorial(n-1)

def sum_into_sequence(current_number , accumulated_sum ):
    if current_number  == 11:
        return accumulated_sum
    return sum_into_sequence(current_number + 1 , accumulated_sum + current_number)    

if __name__ == "__main__":
    # print(factorial(5))  # output 120
    print(sum_into_sequence(1 , 0)) 