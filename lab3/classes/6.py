def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)