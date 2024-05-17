#Lab num 1

print("Hello Profe")


print("Python has three numeric types: int, float, and complex")

#Creating a variable

myValue=1

#Then we are going to print the value of the variable

print(myValue)

#The following is to know the type of the variable

print (type(myValue))

#To combine numbers and text, use the str() built-in function, which converts an argument into a collection of letters called a string. In this instance, you are converting the int (integer) data type into the string data type:

print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=3.14

print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

#Excercise number 4
myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
 
 
#Exercise 5: Introducing the bool data type

myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

#Exercise 1: Introducing the string data type

myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

#The following is to learn how to concatanate str

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#The following is for the function input ()

name = input("What is your name? ")
print(name)

#When your script wants to communicate information back to the user, it is called output. 

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))

