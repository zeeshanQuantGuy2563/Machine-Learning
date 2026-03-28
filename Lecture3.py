#STRINGS {Immuatble Data Type.}

word1="Python is used for"
word2="Machine Learning."

sentence=word1 +" "+word2 #concatenation

print(sentence)

print(word1[4]) #Indexing.

for char in sentence: #Traversal of string.
    print(char)

print(sentence[1:5]) #Slicing of string {string[starting_idx,Ending_idx+1]}

print(sentence[-5:-1]) #Negative indexing is also available in python it runs from -n to -1

a=5
b=10
sum=a+b

print("sum is {}.".format(sum)) #Normal formating and the old ways to do it. (placeholders-> {}, format(placevalues-> replace the place holders))

print("The sum of {} and {} is {}".format(a,b,sum)) #Index based formating and respective assignment.

print("The sum of {1} and {0} is {2}".format(a,b,sum)) #We can choose the index.

print("The value of a is {a} and value of b is {b}.".format(a=3,b=4)) #Value based formating.

print(f"The sum of {a} and {b} is {sum}.") # The F-Strings 

#LISTS {Mutable data type.} {Multiple different types of data can be stored in a string.}

marks=[65,68,90,100,34,45]

print(marks) 

print(len(marks)) #The number of elements in list.
print(type(marks))

print(marks[2]) #Indexing can be done in lists.
print(marks[4])

print(marks[:4]) #Slicing can be done in lists.
print(marks[1:4])

marks[0]=30 #Item assignment can also be done in lists.
marks[5]=60
print(marks)

#List Mehtods

marks.append(34) #Add at the end of the list.

marks.insert(3,50) #Add value at desired index. {The given value is added at index 3 in the list and every other value is pushed back.}

marks.sort() #Arranges it in ascending order. If we write marks.sort(reverse=True) then it will arrange in descending order.

marks.reverse() #reverses the list.

list=[1,2,3,4,8,45,10,34,56,100] #Search in list using the for loop. {Linear Search.}
x=10
i=0
for val in list:
    if(val==10):
        print(i)
        break
    i+=1

#TUPLE {Immutable sequence of values.}
tup=(1,2,3,4,5,6,7,8,9,10)

print(type(tup))

print(len(tup))

print(tup[3]) #Indexing can be done but item assignment is not available.

#for loop operations are same as list.
tu=("abc",) #This comma is necessary to create a single valued tuple.

#slicing can be done.

#TUPLE Methods.

t=(1,2,2,2,3,5,6,8)

t.index(2) #Gives the index at first occurence of value in parentheses.

t.count(2) #Gives the number of elements in tuple of the same value as in the parentheses.

#Dictionary {key(unique):value pairs} {They are by nature mutble.} {They are unordered}

dict={
    "name":"Zeeshan",
    "Age": 18,
    "Sex":"Male"
}

print(dict)

print(type(dict)) #Type -> Dictionary.

print(dict["name"]) #Indexing is in the form of Key-Value pairs.
print(dict["Age"])
print(dict["Sex"])

print(dict.keys()) #Return all the keys.

print(dict.values()) #Return all the values of keys.

print(dict.items()) #Return all the key value pairs.

print(dict.get("name")) #Return a specific value of a key provided in parentheses. {Better then simple indexing}

print(dict.update({
    "city":"Delhi"
})) # add a key value pair.

#SETS {A mutable data type with immutable elements.} {It only stores unique elements.} {it is unordered}

set={1,2,2,2,2,3,44,4,5,5,6,6,6,6,7,7}
set2={1,2,3,4,5,6,7,8,9,0}

print(set)

print(type(set))

empty_set=set() #To create empty set.

set.add(234) #Adds a value in the set.

set.remove(2) #Removes the value provided in the parentheses.

set.clear() #Remove all the elements from the set.

set.pop() #Removes a random value from the set.

set.union(set2) #Gives us the unioun of two sets.

set.intersection(set2) #Gives us the intersection of two sets.

