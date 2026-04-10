# EXCEPTION HANDLING.

try:                                       #The block that is used for the exceptions to occur.
    x=int(input("Enter the divisor: "))
    ans=10/x

except ZeroDivisionError:                  #To provide methods for error.
    print("Divison by zero is not allowed.")

except ValueError:
    print("Invalid input.")

else:                                       #If no exceptions arrise else is executed.
    print(f"ans={ans}")

finally:                                   #It will alwas be executed whether exceptions arise or do not arise.
    print("This is the end of program.")


#List comprehension. [output for item in iterable if condition] {better way to do things}

square= [i*i for i in range(1,6)]
print(square)

sq=[i*i for i in range(1,10) if i%2!=0]
print(sq)

nums=[-2,-4,-5,2,3,4,5,6]

nums=[0 if val<0 else val for val in nums]

print(nums)

words=["hello", "python", "apnacollege"]

words=[char.upper() for char in words]

print(words)