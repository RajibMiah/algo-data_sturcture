def  maxSum(arr , k):
    n = len(arr)
    cur_sum = sum(arr[:k])
    max_sum = cur_sum
    for i in range(n - k):
        cur_sum = cur_sum - arr[i] + arr[i+ k]
        max_sum = max(max_sum , cur_sum)
    return max_sum

    
arr = [1, 7, 2, 11, 20, -8, 0, 0, 20]
k = 3
print(maxSum(arr, k))