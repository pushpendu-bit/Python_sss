import os

# Get the list of all files and folders in the specified directory
contents = os.listdir(r"C:\Users\pushp\OneDrive\Desktop\C++DSA")

# Loop through each item in the directory
for item in contents:
    
    # Print the name of each file or folder
    print(item)