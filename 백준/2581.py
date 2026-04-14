def is_prime(num):
    if num == 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

m = int(input())
n = int(input())

prime_numbers = []

for i in range(m, n + 1):
    if is_prime(i):
        prime_numbers.append(i)

if len(prime_numbers) == 0:
    print(-1)
else:
    print(sum(prime_numbers))
    print(min(prime_numbers))
