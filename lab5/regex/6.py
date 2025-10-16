import re

with open(r"C:\Users\User\Desktop\pp2_labs\lab5\row\row.txt", encoding="utf-8") as f:
    data = f.read()

modified_data = re.sub(r'[ ,.]', ':', data)
print("6:", modified_data)