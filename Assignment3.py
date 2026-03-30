# Question of CLASS. Build a student enrollment system.
#solution:-
info=[
    ("Alice","English"),
    ("Zeeshan","Maths"),
    ("Aditya","Science"),
    ("Bhanu","Social Science"),
    ("Abhinav","ECE"),
    ("Tanmay","Electrical Engineering")
]

# i)
unique_courses=set()
for tup in info:          #Way No.1
    unique_courses.add(tup[1])

print(unique_courses)

for name,courses in info:       #Way No. 2
    unique_courses.add(courses)

print(unique_courses)

# ii)
for tup in info:
    if(tup[1]=="English"):
        print(tup[0])

# iii)
dict={}

for name, courses in info:
    if(dict.get(name)==None):
        dict.update({name : set()})
        dict[name].add(courses)
    else:
        dict[name].add(courses)


print(dict)

#Q1. 
#solution:-
input_string=input("Enter the string :")


def is_palindrome(input_string): #Two pointer approach {Better method}
    st=0
    end=len(input_string)-1
    while(st<end):
        if(input_string[st]!=input_string[end]):
           return "The string is not a palindrome."
        st+=1
        end-=1
    return "The string is a pallindrome."

print(is_palindrome(input_string))     

def is_palindrome1(input_string):  #The list method. {Dumbo method}
    string=[]
    for char in input_string:
        string.append(char)
    reverse=string
    reverse.reverse()
    if(reverse==string):
        return "It is a palindrome."
    else:
        return "It is not a palindrome."

print(is_palindrome1(input_string))

#Q2.
#solution:-

def Average(list):
    sum=0
    for val in list:
        sum+=val
    Avg=sum/len(list)
    return Avg

list=[1,2,3,4,5,6,7,8,9]
print(f"The Average of given list is {Average(list)}")

#Q3. 
#solution:-
list1=list(map(int,input("Enter values seperated by space :").split()))
list2=list(map(int,input("Enter values seperated by space :").split()))

list3=list1 + list2

list3.sort()

print(list3)

#Q4.
#solution:-
tup=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
even_numbers=[]
odd_numbers=[]

for val in tup:
    if(val%2==0):
        even_numbers.append(val)
    else:
        odd_numbers.append(val)

print(f"Even numbers in tuple are: {even_numbers}")

print(f"Odd numbers in tuple are: {odd_numbers}")

#Q5.
#solution:-
student_info={
    "Zeeshan":97,
    "Aditya":87,
    "Bhanu":95,
    "Rajan":80,
    "Abhinav":86,
    "Siddharth":100
}

def menu_based_program(student_info):
    print("'A'- Add a student.")
    print("'B'- Update Marks.")
    print("'C'- Search for student.")
    print("'D'- Display all students and marks.")
    menu=input("Enter the command: ").upper()
    if(menu=='A'):
        student=input("Enter the student's name: ")
        marks=int(input("Enter the marks of student: "))
        student_info.update({student:marks})
        print(student_info)
    if(menu=='B'):
        student=input("Enter the student's name: ")
        updated_marks=int(input("Enter the marks to be updated: "))
        student_info[student]=updated_marks
        print(student_info)
    if(menu=='C'):
      student=input("Enter the student's name: ")
      for search in dict:
        if(search==student):
            print(f"Found with marks: {student_info(student)}")
            break
      print("Not Found...!")
    if(menu=='D'):
        print("All the information of students :")
        print(student_info)

menu_based_program(student_info)

#Q6. 
#solution:-
words =["apple","banana","kiwi","cherry","mango"]

words_length={}

for name in words:
   words_length.update({name:len(name)})

print(words_length)

#Q7:-
#solution:-
string=input("Enter the string: ")
spaces=0
for char in string:
   if(char==' '):
      spaces+=1

print(spaces)

#Q8.
#solution:-
list1 =[1,2,3,4] 
list2 =[5,6,7,8]

list1 =[1,2,3] 
list2 =[3,4]

def is_common(list1,list2):
    for val in list1:
        for val1 in list2:
            if(val==val1):
                return "They have common elements..!!"
    return "No common elements found..!!"

print(is_common(list1,list2))

#Q9. 
#solution:-
list=[1,1,1,4,4,5,5,6,6,4,5,10,10,30,45,11,22]

list.sort()

st=1
count=0

while(st<len(list)):    #Method 1
    if(list[st]==list[st-1]):
        count+=1
    else:
        count=0
    if(count>=2):
        st+=1
        continue
    if(count>=1):
        print(list[st])
    st+=1

set=set(list)     #Method 2
for val in set:
    count=0
    for val1 in list:
        if(val==val1):
            count+=1
    if(count>1):
        print(val)

#Q10.
#solution:-
string=input("Enter the string: ")

#i)
list=[]

for char in string:
    list.append(char)

for char in set(list):
    print(char)

#ii)
for char in set(list):
    print(f"The number of {char} is {list.count(char)}")

