def spy_game(nums):
    code = [0, 0, 7]
    i = 0
    for num in nums:
        if num == code[i]:
            i += 1
            if i == len(code):
                return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))