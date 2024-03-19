# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is line 2.\n")
        file.write("Number 3: 42\n")
except PermissionError:
    print("Error: Insufficient permissions to create the file.")
except Exception as e:
    print(f"An error occurred: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of my_file.txt:")
        print(contents)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is a new line.\n")
        file.write("Another new line.\n")
        file.write("And one more.\n")
except PermissionError:
    print("Error: Insufficient permissions to write to the file.")
except Exception as e:
    print(f"An error occurred: {e}")

print("File handling tasks completed.")
