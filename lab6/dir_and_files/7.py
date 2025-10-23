def copy_file(source, destination):
    with open(source, 'r', encoding='utf-8') as src, open(destination, 'w', encoding='utf-8') as dest:
        dest.write(src.read())

source = input("Enter source file path: ")
destination = input("Enter destination file path: ")
copy_file(source, destination)