def prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
        return True

def fil_prime(num):
    return [n for n in num if prime(n)]
nums=list(map(int,input().split()))
primes=fil_prime(nums)
print(primes)