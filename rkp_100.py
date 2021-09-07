def is_prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2,n):
        if n % i == 0:
            return False

    return True

primes=[x for x in range(2,100) if is_prime(x)]
print(primes)
