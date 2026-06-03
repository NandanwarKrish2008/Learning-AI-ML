import os   # Import the built-in 'os' module to interact with the operating system

# Define the directory path you want to list
# '.' means the current working directory
path = "."  

try:
    # Get a list of all files and folders in the specified directory
    contents = os.listdir(path)

    # Print a header message
    print("Directory contents:")

    # Loop through each item in the directory and print it
    for item in contents:
        print(item)

# Handle the case where the directory does not exist
except FileNotFoundError:
    print(f"Error: The directory '{path}' does not exist.")

# Handle the case where permission is denied
except PermissionError:
    print(f"Error: Permission denied to access '{path}'.")
