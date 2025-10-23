def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

file_path = input("Enter file path: ")
print("Number of lines:", count_lines(file_path))