try:
    data = input("Enter the Sentence : ")
    my_file_1 = open("C:\\python code\\ouput.txt","w")
    for i in data:
        my_file_1.write(i)
    print("File Created.")
except:
    print("FIle not created.")
else:
    my_file_1.close()
    print("Data Successfully written to output.txt.")
    
try:
    addition_data = input("\nEnter the additional data into file : ")
    my_file_1 = open("C:\\python code\\ouput.txt","a")
    my_file_1.write("\n")
    for i in addition_data:
        my_file_1.write(i)
    print("Data Successfully appended.")
except:
    print("Data not Succesfully Appended.")
else:
    my_file_1.close()

    
