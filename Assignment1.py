#Q1.
#solution:-
user_name=input("Enter your name: ")
age=int(input("Enter your age: "))
print("Hello",user_name,",","you are",age,"years old.")

#Q2.
#solutions:-
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))

print(a+b)
print(a-b)
print(a*b)
print(a/b)

a=b,b=a  #Q6. solution of swaping  
print(a)
print(b)

#Q3. 
#solutions:-
int1=int(input("Enter the first integer: "))
int2=int(input("Enter the second integer: "))
float1=float(input("Enter the float number: "))

Avg=(float(int1)+float(int2)+float1)/3

print("The Avg. of the three numbers is:",Avg)


#Q4.
#solutions:-
num=input("Enter a number: ")
int_num=int(num)
float_num=float(num)
string_num=str(num)

print(int_num,type(int_num))
print(float_num,type(float_num))
print(string_num,type(string_num))


# Q5.
# solution:-
x=10+3*2**2
print(x)

#Q7.
#solution:-
CelsiusTemp=input("Enter the temperature in degree celsius: ")

FarenheitTemp=(float(CelsiusTemp)*(9/5))+32

print(FarenheitTemp)

#Q8.
#solution:-
r=float(input("Enter the radius of circle: "))
PI=3.14
Area_of_circle=PI*r**2

print("The area of required circle is:",Area_of_circle)

#Q9.
#solutions:-
P=float(input("Enter the principle: "))
R=float(input("Enter the Rate of Intrest: "))
T=float(input("Enter the time in years: "))

SI=(P*R*T)/100

print("The simple intrest is:",SI)

#Q10.
#solution:-
Decimal_number=float(input("Enter a Decimal number: "))
print("The integer part is:",int(Decimal_number))
print("The decimal part is:",Decimal_number-int(Decimal_number))