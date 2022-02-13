

n = 9000000
prime_list = list()


def sieve(n):
    numbers = [False for i in range(n + 1)]
    p = 2
    while(p * p <= n):
        if(numbers[p] == False):
            for i in range(p ** 2, n + 1, p):
                numbers[i] = True
        p += 1

    numbers[0] = 1
    numbers[1] = 2

    for i in range(2, n + 1):
        if numbers[i] == False:
            prime_list.append(i)

    # print(prime_list , end =' ')

    return prime_list


if __name__ == '__main__':
    prime_numbers = sieve(n)
    input_of_query = int(input('how many queries you want ? '))
    try:
        while(input_of_query):
            q = int(input('Please give finding prime number: '))
            print(prime_numbers[q - 1])
        input_of_query -= 1
    except:
        print('memory limit excecuted')
