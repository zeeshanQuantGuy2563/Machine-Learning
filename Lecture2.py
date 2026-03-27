#Conditional Statements.

#Q1.
#solution:-
username=input("Enter your username: ")
password=input("Enter your Password: ")

if(username=="Admin" and password=="1234567890"):
    print("Login successful.")
else:
    print("An ERROR occured.")

if(username!="Admin"):
    print("Wrong username.")
elif(password!="1234567890"):
    print("Wrong Password.")

#Kind of a better approach by nesting:-
if(username=="Admin"):
    if(password=="1234567890"):
        print("SUCCESS.")
    else:
        print("ERROR..!! Wrong password.")
else:
    print("ERROR..!! Wrong username.")


#Q2.
#solution:-
n=int(input("Enter the number to be checked: "))
if(n%5==0):
    print("The number is a multiple of 5. ")
else:
    print("Not a multiple of 5. ")

#Q3.
#solution:-
n=int(input("Enter the number to be checked: "))
if(n%2==0):
    print("The number is even.")
else:
    print("The number is odd.")

#Q4. Uses of MATCH_CASE.
#solution:-
color=input("Enter the color: ")
match color:
    case "Green":
        print("Go")
    case "Red":
        print("Stop")
    case "Yellow":
        print("Look")
    case _:
        print("Wrong color..!!")


# LOOPS:-

#Q5. Print Hello World five times.
#solution:-
count=0;
while(count<5):
    print("Hello World.")
    count+=1

#print number from 1 to 5.
count=0
while(count<5):
    print(count+1)
    count +=1

#print number from 5 to 1.
count=5
while(count>0):
    print(count)
    count-=1

#Q6. Print table of any integer n.
#solution:-
n=int(input("Enter the number: "))
i=0
while(i<10):
    print(n*(i+1))
    i+=1

#Q7. Working of Break && Continue.
#solution:-
#Print until a multiple of 6 occurs.
i=1
while(i<=10):
    if(i%6==0):
        break    #Get us out of a loop on a condition.  
    print(i)
    i+=1

#Print all numbers except multiple of 3.
i=1
while(i<=10):
    if(i%3==0):
        i+=1
        continue  #Skip current iteration.
    print(i)
    i+=1

#Q8. Print all the odd numbers from 1 to 10.
i=1
while(i<=10):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1

i=1
while(i<=10):
    if(i%2!=0):
        print(i)
    i+=1

#Better Approach
i=0
while(i<10):
    i+=1
    if(i%2==0):
        continue
    print(i)

#Q9. Traversal of string.

string="ZeeshanAhmadAnsari"
for char in string:   #in -> Membership operator. {Also used to check presence.}
    print(char)

if 'o' in string:
    print(" 'o' Exist in string. ")


#The Range Function.  range(0 to n-1) {Sequence Generation.} range(start{(optional) Default=1}, stop{compulsory}, step{(optional)Default=+1}))
#The count of i in word.

word="Artificialintelligence"
ans=0
for char in word:
    if(char=="i"):
        ans+=1
print("The number of i's in word is:",ans)


#Q10. Print the vowel count of a given string.
#solution:-
word="artificialintelligence"
vowel_count=0
for char in word:
    if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
        vowel_count+=1
print("The total number of vowels in word is :",vowel_count)


#Q11. The sum of first 'N' natural numbers.
#solutions:-
n=int(input("Enter the value of N: "))
if(n<=0):
    print("ERROR...! the value of N cannot be negatibe or zero.")
else:
    sum=0
    for i in range(1,n+1):
        sum+=i
    print("The sum of first Nnatural numbers is :", sum)


#FUNCTIONS. {def Function_name(parameters)}


#Q12. WAF to print the Avg. of three numbers.
# solution:-
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))

def Average_of_three(a,b,c): #We can also create default variables {non_default parameters, default parameters} -> avg(a,b,c=1)
    Avg=(a+b+c)/3
    return Avg

print("The Average of the three given numbers is :",Average_of_three(a,b,c))

#Lambda Functions:- {single liner functions }

sum= lambda a,b:a+b
print(sum(1,5))

#Q13. WAF to print the factorial of number N.
#solution:-
n=int(input("Enter the value of N: "))

def factorial(n):
    if(n<0):
        return "ERROR..!! negative numbers not allowed."
    if(n==0):
        return 1
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

print("The factorial of desired number is :",factorial(n))

