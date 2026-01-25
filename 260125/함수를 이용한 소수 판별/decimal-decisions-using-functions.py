def sum_primes(a, b):
    total_sum = 0
    for i in range(a, b + 1):
        is_prime = True 
        for j in range(2, i):
            if i % j == 0:
                is_prime = False 
                break 
        if is_prime:
            total_sum += i
    print(total_sum)

a, b = map(int, input().split())
sum_primes(a, b)
