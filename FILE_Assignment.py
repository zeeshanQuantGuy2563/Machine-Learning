#Q1.
#solution:-

with open("names.txt",'w')as f:
    i=0
    while(i<5):
        name=input("Enter the name: ")
        i+=1
        f.write(f"{name}\n")

with open("names.txt",'r') as f:
    print(f.read())

#Q2.
#solution:-

with open("log.txt",'a') as f:
    f.write("Program Run successfully.")

with open("log.txt",'r') as f:
    print(f.read())

#Q3.
#solution:-
l=[5,10,15,20,25]

list=[val for val in l if val>15]

print(list)

#Q4.
#solution:-
import json

dict={
    "Delhi":3000000,
    "Uttrakhand":5000000,
    "Uttarpradesh":2000000
}

with open("cities.json",'w') as f:
    json.dump(dict, f)

new_city=input("Enter the name of city: ")
new_pop=int(input("Enter the population: "))

dict.update({new_city:new_pop})

with open("cities.json",'w') as f:
    json.dump(dict,f, indent=4)

with open("cities.json",'r')as f:
    data=json.load(f)
    for cities,population in data.items():
        print(f"{cities}:{population}")
    

#Q5.
#solution:-
try:
    with open("data.txt",'r') as f:
        data=f.read()

except FileNotFoundError:
    print("File not found in the system.")

else:
    print(data)

finally:
    print("The program has ended.")
