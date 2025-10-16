import re

with open(r"C:\Users\User\Desktop\pp2_labs\lab5\row\row.txt", encoding="utf-8") as f:
    data = f.read()

modified_data = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), data)
print("7:", modified_data)