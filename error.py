# Error Handling Lab
filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        print("File content:")
        print(file.read())
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read the file '{filename}'.")
except IOError:
    print(f"Error: An unexpected error occurred while accessing '{filename}'.")
