#file handling

#writing to a file

with open("example.txt", "w") as file:
    file.write("Hello, World!")

#reading from a file

with open("example.txt", "r") as file:
    print(file.read())

#closing a file
file.close()

#append to a file

with open("example.txt", "a") as file:
    file.write("Hello, World!")

#reading from a file

with open("example.txt", "r") as file:
    print(file.read())

#closing a file
file.close()