
def findOccurrence(str, ptr):
    n = len(str)
    k = len(ptr)
    freq = {}
    for i in ptr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] =1
    i = 0
    j = 0
    count = len(freq)
    ans = 0
    while(j < n):
        if str[j] in freq:
            freq[str[j]] -= 1
            if freq[str[j]] == 0:
                count -= 1 
        if (j - i + 1 < k):
            j +=1
        elif(j - i + 1 == k):
            if count == 0:
                ans += 1
            i += 1    
            if str[i] in freq:
                freq[str[i]] += 1
                if freq[str[i]] == 1:
                    count += 1
            j += 1  
    return ans

print(findOccurrence("forxforxorfxforpxfro" ,"for"))