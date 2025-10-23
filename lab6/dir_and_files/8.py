import os

def delete_file(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("File deleted.")
    else:
        print("Cannot delete file. Check if it exists and is writable.")

file_path = input("Enter file path to delete: ")
delete_file(file_path)