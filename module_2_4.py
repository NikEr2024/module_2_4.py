numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for number in numbers:
    if numbers == 1:
        continue
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            for i in primes:
                if i == 1:
                    primes.remove(i)
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print('primes',primes)
print('not_primes',not_primes)
