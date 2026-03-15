"""#lab assignment 1
# Program to copy text from one file to another in uppercase
source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")
with open(source_file, "r") as f1:
    content = f1.read()
upper_content = content.upper()
with open(destination_file, "w") as f2:
    f2.write(upper_content)
print("\nContent copied successfully in UPPERCASE!\n")
print("Source File Content:")
print(content)
print("\nDestination File Content:")
print(upper_content)
"""
#lab assignment 2
# Program to copy python script without comments
source = input("Enter source python file name: ")
destination = input("Enter destination file name: ")
with open(source, "r") as f1, open(destination, "w") as f2:
    for line in f1:
        line = line.strip()
        if line.startswith("#") or line == "":
            continue
        f2.write(line + "\n")
print("\nFile copied without comments successfully!\n")
print("Source File Content:")
with open(source, "r") as f:
    print(f.read())
print("\nDestination File Content (Without Comments):")
with open(destination, "r") as f:
    print(f.read())