# File handling: .txt

# Reading Files:
# file_path = r"C:\Users\neepal\PycharmProjects\Batch4SeleniumPython\PythonPrograms\example.txt"
#
# with open(file_path, "r") as file:
#     contents = file.read()
#     print(contents)

# Explanation:
# open(): Opens the file specified by file_path in read mode ("r").
# with: Ensures the file is properly closed after reading.
# read(): Reads the entire contents of the file into a string variable.

# 2 Reading line by line:
# file_path = r"C:\Users\neepal\PycharmProjects\Batch4SeleniumPython\PythonPrograms\example.txt"
#
# with open(file_path, "r") as file:
#     for line in file:
#         print(line.strip())  # Strip removes any trailing whitespace, including the newline character


# Write to files:
# file_path = r"C:\Users\neepal\PycharmProjects\Batch4SeleniumPython\PythonPrograms\example11.txt"
#
# with open(file_path, "w") as file:
#     file.write("THIS IS ALL ABOUT WRITING IN NOTEPAD FILE\n")
#     file.write("THIS IS ANOTHER LINE IN NOTEPAD FILE")

# Explanation:
# open(): Opens the file specified by file_path in write mode ("w"). If the file doesn't exist, it will be created.
# write(): Writes the specified content to the file. \n is used to indicate a newline.

# Append the content to exisiting file:
file_path = r"C:\Users\neepal\PycharmProjects\Batch4SeleniumPython\PythonPrograms\example11.txt"
with open(file_path, "a") as file:
    file.write("\nI am having fun learning python!")

file.close()