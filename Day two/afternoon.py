#dictionaries
#Dictionaries cannot have two items with the same key:
#Dictionaries are changeable, meaning that we can change, 
#add or remove items after the dictionary has been created


dict = {
  "name": "iPhone",
  "model": "iPhone14",
  "year": 2022
}
print(dict)

#length of the dictionary
print(len(dict))

#datatype of the dictionary
print(type(dict))



#accessing the dictionary
z=dict["year"]  
print(z)

#adding a new key-value pair to the dictionary
dict["color"] = "black"
print(dict)

#deleting a key-value pair from the dictionary
del dict["color"]
print(dict)


#Exercise ONE
#Use the value function to return all values in the dictionary
car = {
"brand": "Benz",
"model": "S Class",
"year": 1999
}
print(car.values())


#EXERCISE TWO-If the key exists in the dictionary
car = {
"brand": "Benz",
"model": "S Class",
"year": 1999
}
print(car.get("brand"))

#EXERCISE THREE - How to change the dictionary items
cars = {
"brand": "Benz",
"model": "S Class",
"year": 1999
}
cars["year"] = 2020
print(cars)

#update the dictionary items
vehicle= {
"brand": "Benz",
"model": "S Class",
"year": 1999
}
vehicle.update({"year": 2020})
print(vehicle)

#EXERCISE 4- how to add and remove items from the dictionary of fruits
#add items to the dictionary
fruit = {
  "name": "banana",
  "color": "yellow",
  "size": 7
}
fruit["shape"] = "cylindrical"
print(fruit)

#remove items from the dictionary 
del fruit["color"]
print(fruit)

#EXERCISE 5-Loop through and nested dictionaries
#loop through the dictionary
fruit = {
  "name": "banana",
  "color": "yellow",
  "size": 7
}
for x in fruit:
  print(fruit[x])

  #Nested 
  Secondary = {
  "teacher1" : {
    "name" : "Phad",
    "year" : 2004
  },
  "teacher2" : {
    "name" : "Haler",
    "year" : 2007
  },
  "teacher3" : {
    "name" : "Fin",
    "year" : 2011
  }
}

print(Secondary["teacher1"]["name"])










