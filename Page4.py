#This i for the page 4

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#In programming languages, the list position starts at zero (0). The brackets tell Python which position in the list you want.

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#In Python, list position starts at zero (0), so you must use the numeral 2 to access the third position

myFruitList[2] = "orange"
print(myFruitList)

#Defining a tuple
#The tuple is like a list, but it can't be changed. A data type that can't be changed after it's created is said to be immutable. To define a tuple, you use parentheses instead of brackets ([]).

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#Defining a dictionary
#A dictionary is a list with named positions (keys). Imagine that your list shows people’s favorite fruit.

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])