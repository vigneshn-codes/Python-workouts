#file handling and directory

#creating a directory
import os
os.mkdir("example_directory")

#listing a directory
print('Listing directory:', os.listdir("example_directory"))

#removing a directory
os.rmdir("example_directory")

#checking if a directory exists
print('Directory exists:', os.path.exists("example_directory"))

#checking if a file exists
print('File exists:', os.path.exists("example.txt"))

#checking if a directory is empty
print('Directory is empty:', os.path.isdir("example_directory"))

#checking if a file is empty
print('File is empty:', os.path.isfile("example.txt"))

#checking if a directory is empty
print('Directory is empty:', os.path.isdir("example_directory"))

#checking if a file is empty
print('File is empty:', os.path.isfile("example.txt"))

#checking if a directory is empty
print('Directory is empty:', os.path.isdir("example_directory"))