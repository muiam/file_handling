try:
    with open('my_file2.txt', 'r') as file:
        contents = file.read()
    print("Contents of the file:")
    print(contents)
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("Permission denied.")
finally:
    print("Operation completed.")