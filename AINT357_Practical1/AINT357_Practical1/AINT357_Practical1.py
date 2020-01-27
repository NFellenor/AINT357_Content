#Practical 1 -AINT357 - Python:

#python-course.eu
#w3schools.com/python/default.asp

#Print statement directly to command line:
print("Hello.")
#NOTE: Can also create Python in file on server using .py extension and running it in command line.

#Simple IF statement:
if 10 > 5:
		print("Yes, 10 is > 5.")

#Creating variables:
x = 1
print(x)
print("This is a written print statement including a variable: ", x)

#Data types: 
#TEXT TYPE: str
#NUMERIC TYPE: int, float, complex
#SEQUENCE TYPE: list, tuple, range
#MAPPING TYPE: dict
#SET TYPE: set, frozenset
#BOOLEAN TYPE: bool
#BINARY TYPE: bytes, bytearray, memoryview

#Get data type:
print("Variable x is a ", type(x), "data type.")
#NOTE: Most common data types (text, numeric) are assigned when the variable is declared

#Casting: Specify a type onto a variable
y = int(1)
z = str(3.0) #Maybe more useful 
print("Variable z is", type(z), "data type")

#String literal
print('Oi') #Single quotations
#or
test = 'Hey.'
print(test)
#Multiline string can be assigned to variable using """...""" or multiline literal '''...'''

#Booleans: Most booleans are true. An empty string, or 0, are false.
print(10 > 9) #Will print true of false
print(9 > 10)
#another example:
m = 15
n = 30

if n == 2*m: #2 multiplied by m
	print("Yeh mate it's true 15x2=30...")
else: 
	print("Nah.")

#Operators:
m + n #Addition
m - n #Subtraction
m * n #Multiplication
m / n #Division
m % n #Modulus
m ** n #Exponential 
m // n #Floor division

#The 4 types of Python array / collection:
#List, Tuple, Set, Dictionary
#List type:
animalList = ["dog", "cat", "crocodile"]
print(animalList)
#To refer to specific items, use [x], so [0] = first item, [-1] = last item, [-2] = second to last etc.
print(animalList[0]) #Print dog
#Use : in selector to specify range from x to y or end of list or from start:
print(animalList[1:]) #Print from second item to end
animalList[2] = "alligator" #Change list item [2] to alligator 
print(animalList)

#Loop through list:
for x in animalList:
	print(x) #Print each value in list

#Check for item in list
if "cat" in animalList:
	print("Cat is in list")
else:
	print("Cat not in list")

print(len(animalList)) #List length

#Add/remove from list:
animalList.append("frog") #Add frog to end of list
print(animalList) 
animalList.insert(0, "chicken") #Insert chicken at specified index in list
print(animalList)

animalList.remove("frog") #Remove specified item
print(animalList)
animalList.pop(0) #Remove item by specifying index
print(animalList) 

#Copy list using .copy
#TO DO: Add tuples sets and dictionary examples

#While loop syntax:
i = 1
while i < 6:
	print(i)
	i += 1

#Function declaration and example
def function(animal): #Declare with argument "animal" which is passed into when called
	print("This is printed from within the function function. " + animal)

function("parrot") #Call 





















