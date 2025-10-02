
def permute(s, l, r):
    if l == r:
        print(''.join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]

def print_permutations():
    user_input = input("Enter a string: ")
    s_list = list(user_input)
    permute(s_list, 0, len(s_list) - 1)

print_permutations()