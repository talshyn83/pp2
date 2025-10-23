from functools import reduce

def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst, 1)

nums = [2, 3, 4, 5]
print("Product:", multiply_list(nums))