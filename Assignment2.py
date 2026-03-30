#Q1.
#solution:-
salary=int(input("Enter the salary amount: "))
if(salary<0):
    print("Please..Enter a valid salary amount.")
else:
    if(salary<30000):
        print("The final tax rate would be 5% and the tax amount will be", 0.05*salary)
    elif(salary>=30000 and salary<=70000):
        print("The final tax rate would be 15% the tax amount will be", 0.15*salary)
    else:
        print("The final tax rate would be 25% the tax amount will be", 0.25*salary)

#Q2. 
#solution:-
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))

def print_even(a,b):
    for i in range(a,b+1):
        if(i%2==0):
            print(i)

print("All the even numbers between",a,",",b,"are :")
print_even(a,b)

#Q3. 
#solution:-
num=int(input("Enter the number :"))

def print_digits(num):
    while(num>0):
        print(num%10)
        a=int(num/10)
        num=a

print("All the digits of the given number is: ")
print_digits(num)

#Q4. 
#solution:-
num=int(input("Enter the number :"))

def count_digits(num):
    count=0
    while(num>0):
        count+=1
        a=int(num/10)
        num=a
    return count

print("The numer of digits in",num,"is",count_digits(num))

#Q5. 
#solution:-
num=int(input("Enter the number :"))

def sum_of_digits(num):
    sum=0
    while(num>0):
        sum+=num%10
        a=int(num/10)
        num=a
    return sum

print("The sum of digits of the given number is :", sum_of_digits(num))

#Q6.
#solution:-
def numbers():
    for i in range(1,101):
        if(i%3==0 and i%5==0):
            print(i)

print("The numbers divisible by 3 and 5 are :")
numbers()

#Q7.
# solution:-
while(True):
    n=input("Enter the number: ")
    if(n=="Quit"):
        break
    if(int(n)<0):
        print("The given number is negative.")
    elif(int(n)==0):
        print("The given number is neutral.")
    else:
        print("The given number is positive.")

#Q8. 
#solution:-
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
operation=input("Enter the operation: ")

def calculator(a,b,operation):
    if(operation=='+'):
        print("The sum is:",a+b)
    elif(operation=='-'):
        print("The difference is:",a-b)
    elif(operation=='*'):
        print("The product is:",a*b)
    elif(operation=='/'):
        print("The quotient is:",a/b)
    else:
        print("ERROR..!! Invalid operation.")

calculator(a,b,operation)

#Q9.
#solution:-
num=int(input("Enter the number: "))

def is_prime(num):
    if(num==1 or num==2):
        return True
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

if(is_prime(num)==True):
    print("The given number is prime.")
else:
    print("The given number is not prime.")

#Q10.
#solution:-
print("You have Entered the NUMBER GUESSING GAME.")
Given_number=10
while(True):
    num=int(input("Guess the number: "))
    if(num>Given_number):
        print("Too high..!!")
    elif(num<Given_number):
        print("Too low..!!")
    else:
        print("Correct..!!")
        break

