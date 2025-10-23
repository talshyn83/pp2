def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("Upper case letters:", upper)
    print("Lower case letters:", lower)

s = input("Enter a string: ")
count_case(s)