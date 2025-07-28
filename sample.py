1# File creation....
# try:
#     my_file = open("C:\\python code\\sample.txt","w")
#     my_file.write("This is sample text file.\n It contains multiple lines.")
#     print("File created.")
# except:
#     my_file.close()
#     print("File not created.")

2# Reading File....
try:
    with open("C:\\python code\\sample.txt","r") as file_1:
        print(file_1.read(100))
except:
    print("The file sample.txt was not found.")
else:
    file_1.close()
    print("File read successfully.")
    