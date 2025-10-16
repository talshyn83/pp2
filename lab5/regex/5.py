import re

with open(r"C:\Users\User\Desktop\pp2_labs\lab5\row\row.txt", encoding="utf-8") as f:
    data = f.read()

matches = re.findall(r'a.*b', data)
print("5:", matches)