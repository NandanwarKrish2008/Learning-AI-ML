import os

# Specify the directory path (use '.' for current directory)
path = "."  

try:
    contents = os.listdir(path)
    print("Directory contents:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"Error: The directory '{path}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access '{path}'.")
