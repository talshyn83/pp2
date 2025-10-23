def write_list_to_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(str(item) + '\n')

data = ["Hello", "World", "Python"]
file_path = input("Enter file path: ")
write_list_to_file(file_path, data)