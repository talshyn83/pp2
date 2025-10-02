def reverse():
    s = input()
    reversed_sentence = ' '.join(s.split()[::-1])
    return reversed_sentence

print(reverse())