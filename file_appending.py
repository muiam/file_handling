try:
    with open('my_file.txt', 'a') as file:
        file.write("\nThis is an appended line.\n")
        file.write("Another appended line.\n")
        file.write("Anded one more line to test again line.\n")
        file.write("5 + 10 is not 510. Its just 15 ")
    print("Text appended to the file successfully.")
except IOError as e:
    print(f"Error: {e}")