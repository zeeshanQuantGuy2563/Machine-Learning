#File operations.

#Read the file:-

f=open("sample.txt",'r') # instead of data.txt we should write the file path. {This function open the file}
                        # this will provide a file object

# print(f.readline()) #This function prints the frist line and moves the cursor to the second line.

# print(f.readline())

data=f.read() #To print the data

print(data)

print(type(data)) # types will be string {str}.

f.close() #This is done to prevent the file from unexpected changes.


f=open("sample.txt",'w') #'w' attribute is used for editing.{File truncate is applicable}

f.write("Zeeshan is a good boy. \nHe is good at gaming.") #This function truncates the whole file.

f.close()

# 'a' is the append mode of the open function which lets us append text from the end of the text in file.

# 'x' it creates a new file and open it for writing. {This will create an entirely new file and will help us not to destroy our data accidently}

# 'b' opens the file in binary mode.

# 't' this is the text mode {also considered to be the default}

# '+' opens disk file for updation(r & w)

# WITH KEYWORD

with open("sample.txt","r") as f: #It handels all the opening and closing of data at all times.
    data=f.read()
    print(data)
    print(len(data))

# DELETE FILES

import os

os.remove("sample.txt")

#Q. Find the target word in the line.
#solution:-

with open("sample.txt",'r') as f:
    i=1
    while(True):
        data=f.readline()
        if 'X' in data:
            print(f"The string lies in line no. {i}.")
            break
        i+=1
        if(i>3):
            print("Word not found.")
            break

