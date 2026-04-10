class student:
    def __init__(self, name, cgpa):
        self.name=name
        self.cgpa=cgpa
    subject="python"
    college="ABC"
    year="4th year"


a=10
stu1= student("Zeeshan",9.0)
stu2= student("Rajan",8.0)
stu3= student("Bhanu",7.0)
stu4= student("Abhinav",9.8)
print (stu3.name)
print (stu2.name)
print (stu1.name)
print (stu4.cgpa)
print(stu1.college)
print(stu1.subject)
print(stu1.year)


class student:
    def __init__(self, name, cgpa, pincode): #parameterised constructor
        self.name=name
        self.cgpa=cgpa
        self.pincode=pincode
    
    def get_info(self):
        return self.pincode;

stu1=student("Zeeshan",9.0,110045)
stu2=student("Bhanu", 9.8, 110056)

print(f"{stu1.name} has the cpga {stu1.cgpa} and lives in {stu1.get_info()}.")

print(f"{stu2.name} has the cpga {stu2.cgpa} and lives in {stu2.get_info()}.")

class laptop:
    storage_type="ssd"
    #@classmethod-> this is a decorator that converts instance mthods into class methods.

    def __init__(self, RAM, storage): #Consructor.
        self.RAM=RAM
        self.storage=storage

    def get_storage_info(cls):  #Class methods.
        print(f"storage type ={cls.storage_type}.")
    
    def get_info(self): #Instance method.
        print(f"This laptop has {self.RAM} RAM and {self.storage} {self.storage_type}.")
    
    @staticmethod
    def calc_discount(price, discount):
        final_price=price-price*(discount/100)
        print(f"Discounted price= {final_price}")

l1=laptop("16GB", "256GB") 
l2=laptop("24GB", "512GB")

l1.get_storage_info()
l2.get_storage_info()

l1.get_info()
l2.get_info()

l1.calc_discount(40_000,10)

#PRODUCT STORE.

class Product:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1
    
    def get_info(self):
        print(f"The {self.name} has the price Rs.{self.price}.")
    
    @classmethod
    def get_count_product(cls):
        print(f"The total number of products is {cls.count}.")
    
    @staticmethod
    def discounted_price(price, discount):
        print(f"The discounted price is {price-price*(discount/100)}.")
    
p1=Product("Mobile", 40_000)
p2=Product("Laptop", 1_00_000)
p3=Product("TV", 30_000)

Product.get_count_product()

p1.get_info()
p2.get_info()
p3.get_info()

p1.discounted_price(p1.price, 10)
p2.discounted_price(p2.price, 5)
p3.discounted_price(p3.price, 15)

#The Four pillar of OOPs are Encapsulation, Abstraction, Inheritence, and Polymorphism :-

#Encapsulation:- Wrapping data and functions into a single unit. {The data is not truly private.}

class BankAccount:
    def __init__(self, name, balance):
        self.name=name
        self.__balance=balance #Private attribute can be defined by {__Name_of_attribute}. Protected attribute can be defined as {_Name_of_attribute}.

    
    def get_balance(self): #getter function.-> provides access to the private attribute.
        return self.__balance
    
    def update_balance(self, newbalance): #Setter function.-> provides access to the change of private attribute.
        self.__balance=newbalance
    
acc1= BankAccount("Zeeshan",200_000)

print(acc1.get_balance())

acc1.update_balance(300_000)

print(acc1.get_balance())
    
print(acc1._BankAccount__balance) #Another way of accessing the private attribute.

#Inheritence:- Reusing the attributes and methods of parent(base) class in a child class.

class employee:
    start_time= "10AM"
    end_time="6PM"

class Teacher(employee):
    def __init__(self, subject):
        self.subject=subject
    
    def get_info(self):
        print(f"The subject of techer is {self.subject} and the working hours will be {employee.start_time} to {employee.end_time}.")

te1=Teacher("Maths")

te1.get_info()

# TYPE OF INHERITENCES:-

# i) Single level inheritence:- from a parent to a single child. {Demonstrated in above examples.}

# ii) Multi-level inheritence :- from a parent class to a child class to another child class. {parent-> child-> child}
# Example:- 
class Employee:
    start_time="10AM"
    end_time="2PM"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role=role
    
class Accountant(AdminStaff):
    def __init__(self,role ,salary):
        super().__init__(role)
        self.salary=salary

acc1= Accountant("CA", 3_00_000)

print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)


# iii) Multiple inheritence :- attributes can be inherited from two or more parent class.
# Example:-
class Teacher:
    def __init__(self, salary):
        self.salary=salary

class Student:
    def __init__(self, gpa):
        self.gpa=gpa

class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name=name

ta1= TA(15_000, 9.0, "Zeeshan")

print(ta1.name, ta1.gpa, ta1.salary)

# Abstraction:- Hiding internal details and showing only essential features.

from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar")

# Polymorphism:- a single varibale or operation has different works.

class Teacher:
    def get_designation(self):
        print("Designation= Teacher.")

class Accountant(Teacher):
    def get_designation(self):
        print("Designation= Accountant.")

t1= Accountant()

t1.get_designation()

