def numbers(n):
    for i in range(n,-1,-1):
        yield i

n = int(input())
for num in numbers(n):
    print(num)