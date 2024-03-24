try:
    with open('my_file1.txt', 'w') as file:
        file.write("This is the first line.\n")
        file.write("Here's a number to test writing: 42\n")
        file.write("This is the third line.\n")
    print("File created and written successfully.")
except IOError as e:
    print(f"Error: {e}")