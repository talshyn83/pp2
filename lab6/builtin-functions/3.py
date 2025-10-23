def is_palindrome(s):
    return s == s[::-1]

s = input("Enter a string: ")
print("Palindrome:", is_palindrome(s))