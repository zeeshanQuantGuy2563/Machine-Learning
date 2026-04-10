#Q1.
#solution:-
class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number=account_number
        self.owner_name=owner_name
        self.balance=balance
    
    def deposit(self, amount):
        if(amount<=0):
            print("ERROR...!! Invalid deposit amount.")
        else:
            self.balance+= amount
            print(f"The new account balace is Rs.{self.balance}.")
    
    def withdraw(self, amount):
        if(amount>self.balance):
            print("Insufficient balance.")
        else:
            self.balance-=amount
            print(f"The new account balance is Rs.{self.balance}.")
    
    def check_balance(self):
        print(f"The current balace of the account is Rs.{self.balance}.")

acc1=BankAccount(11004567,"Zeeshan",1_00_000)
acc2=BankAccount(11234578,"Bhanu",2_00_000)
acc3=BankAccount(11028365,"Rajan",4_00_000)

acc1.check_balance()
acc1.deposit(3_00_000)
acc1.withdraw(50_000)

#Q2.
#solution:-
class Book:
    def __init__(self, title, author, list_of_reviews):
        self.title=title
        self.author=author
        self.list_of_reviews=list_of_reviews
    
    def add_review(self, review):
        self.list_of_reviews.append(review)
    
    def count_reviews(self):
        print(f"The number of reviews are {len(self.list_of_reviews)}.")
    
    def display_reviews(self):
        print("The reviews are :")
        print(self.list_of_reviews)

book1=Book("Tower of God", "Zeeshan", ["best book","good book","great book","bad book"])

book1.add_review("Medium level book")
book1.count_reviews()
book1.display_reviews()

#Q3.
#solution:-
class Student:
    def __init__(self, name, roll_number, marks):
        self.__name=name
        self.__roll_number=roll_number
        self.__marks=marks

    def get_info(self):
        return [self.__name, self.__roll_number, self.__marks]
    
    def set_roll_number(self,new_roll_number):
        if(new_roll_number<=0 or new_roll_number>100):
            print("ERROR...! Enter a number between 1 and 100.")
        else:
            self.__roll_number=new_roll_number
    
    def set_marks(self, new_marks):
        if(new_marks<0):
            print("ERROR..! Enter valid marks.")
        else:
            self.__marks=new_marks

    def set_name(self,new_name):
        self.__name=new_name
    
  
stu1=Student("Zeeshan",10, 90)
stu1.set_roll_number(90)
stu1.set_name("Bhanu")
stu1.set_marks(32)
    
print(stu1.get_info())

#Q4.
#solution:-
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    
    def area(self):
        print(f"The area of the circle is {3.14*(self.radius)**2} sq. units.")
    
class Rectangle(Shape):
    def __init__(self, length, bredth):
        self.length=length
        self.bredth=bredth
    
    def area(self):
        print(f"The area of rectangle is {self.length*self.bredth} sq. units.")

class Triangle(Shape):
    def __init__(self,base_length, perpendicular_length):
        self.base_length=base_length
        self.perpendicular_lenght=perpendicular_length
    
    def area(self):
        print(f"The are os the triangle is {0.5*self.base_length*self.perpendicular_lenght} sq. units.")

c1=Circle(10)
r1=Rectangle(20,30)
t1=Triangle(20,30)
c1.area()
r1.area()
t1.area()

#Q5. 
#solution:-
class Vehicle:
    brand="Suzuki"
    Model="z1X"

class Car(Vehicle):
    def __init__(self,seats):
        self.seats=seats
    
    def get_info(self):
        print(f"The car is of brand {Vehicle.brand} and model {Vehicle.Model} and has a total of {self.seats} seats.")

class Bike(Vehicle):
    def __init__(self, engine_cc):
        self.engine_cc=engine_cc
    
    def get_info(self):
        print(f"The bike is of brand {Vehicle.brand} and of model {Vehicle.Model} and has a displacement of {self.engine_cc}cc.")

car1=Car(6)
bike1=Bike(500)

car1.get_info()
bike1.get_info()

#Q6.
#solution:-
from abc import ABC, abstractmethod
class Employee(ABC):
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        salary=1_00_000
        print(salary)

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        salary=2_00_000
        print(salary)

class ContractEmployee(Employee):
    def calculate_salary(self):
        salary=1_50_000
        print(salary)

i1=Intern()
f1=FullTimeEmployee()
c1=ContractEmployee()

i1.calculate_salary()
f1.calculate_salary()
c1.calculate_salary()

#Q7.
#solution:-
class Person:
    def __init__(self,name,age=18,address=110045):
        self.name=name
        self.age=age
        self.address=address
    
    def get_info(self):
        print(self.name)
        print(self.age)
        print(self.address)

p1=Person("Zeeshan")
p2=Person("Bhanu",20)
p3=Person("Rajan",40,110056)

p1.get_info()
p2.get_info()
p3.get_info()

#Q8.
#solution:-
class Player:
    player_count=0

    def __init__(self, name, level):
        self.name=name
        self.level=level
        Player.player_count+=1
    
    def get_info(self):
        print(f"The name of player is {self.name} and level is {self.level}.")

    @staticmethod
    def players():
        print(f"The number of players is {Player.player_count}.")

p1=Player("Zeeshan", 32)
p2=Player("Bhanu",55)
p3=Player("Abhinav", 65)

p1.get_info()
p2.get_info()
p3.get_info()

p1.players()

#Q9.
#solution:-
class Herbivore:
    behaviour="They eat grass."

class Carnivour:
    behaviour="They eat Meat."

class Omnivore:
    behaviour="They eat both plants and animals."

class Bear(Herbivore, Carnivour, Omnivore):
    def get_info(self):
        print(Herbivore.behaviour, Carnivour.behaviour, Omnivore.behaviour)

b1=Bear()

b1.get_info()


#Q10. MINI project - OOP chat system.
#solution:-
class User:
    def __init__(self, name):
        self.name=name

class ChatRoom:
    def __init__(self):
        self.message_history=[]
        self.active_users=[]

    def join(self, user):
        if user not in self.active_users:
            self.active_users.append(user)
            print(f"{user.name} has joined that chat.")

    def leave(self,user):
        if user in self.active_users:
            self.active_users.remove(user)
            print(f"{user.name} has left the chat.")
    
    def send_message(self,user, msg):
        if user in self.active_users:
            print(f"{user.name}:{msg.msg}")
            self.message_history.append(f"{user.name}:{msg.msg}")
        else:
            print("ERROR..! User not found in chatroom.")
    
    def chat_history(self):
        print(self.message_history)

class Message:
    def __init__(self,msg):
        self.msg=msg 

chatroom=ChatRoom()

user1=User("Zeeshan")
user2=User("Bhanu")

chatroom.join(user1)
chatroom.join(user2)

msg1=Message("You are a good friend")
msg2=Message("I feel the same way about you.")

chatroom.send_message(user1,msg1)
chatroom.send_message(user2,msg2)

chatroom.chat_history()

chatroom.leave(user1)
chatroom.leave(user2)