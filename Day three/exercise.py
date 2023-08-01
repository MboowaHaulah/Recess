#EXERCISE ONE
#Create a list with 5 items (names of people) and write a python program to output the 2nditem
names = ["Haulah", "Samir", "Germner", "Hoods", "Pacito"]
print(names[1])

#EXERCISE TWO
#Write a python program to change the value of the first item to a new value
names = ["Haulah", "Samir", "Germner", "Hoods", "Pacito"]
print(names[0])
names[0] = "Germner"
print(names[0])

#EXERCISE THREE
#Write a python program to change the value of the first item to a new value
names = ["Haulah", "Samir", "Germner", "Hoods", "Pacito"]
print(names[0])
names[0] = "Mboowa"
print(names[0])

#EXERCISE FOUR  
#Write a python program to add a sixth item to the list of items
names = ["Haulah", "Samir", "Germner", "Hoods", "Pacito"]
names.append("Nidah")
print(names)

#EXERCISE FIVE
#Write a python program to m to add “Bathel” as the 3rd item in your list
names = ["Haulah", "Samir", "Germner", "Hoods", "Pacito"]
names.insert(2, "Bathel")
print(names)

#EXERCISE SIX
#Write a python program to remove the 4th item from the list
names = ["Haulah", "Samir", "Germner", "Hoods", "Pacito"]
names.remove("Pacito")
print(names)

#EXERCISE SEVEN
# Use negative indexing to print the last item in your list
names = ["Haulah", "Samir", "Germner", "Hoods", "Pacito"]
print(names[-1])

#EXERCISE EIGHT
#Create a new list with 7 fruit items and use a range of indexes to print the 3rd, 4th and 5th items
fruits = [ "orange","mango","banana","kiwi","berry","pawpaw","jackfruit"]

print(fruits[2:6])



#EXERCISE NINE
#Write a list of countries and make a copy of it.
countries = ["Namibia", "Russia", "Tanzania", "Uganda", "Rwanda", "Burundi"]
countries_copy = countries.copy()
print(countries_copy)

#EXERCISE TEN
#Write a python program to loop through the list of countries
countries = ["Namibia", "Russia", "Tanzania", "Uganda", "Rwanda", "Burundi"]
for x in countries:
    print(x) 


#EXERCISE ELEVEN
#Write a list of animal names and sort them in both descending order 
animals = ["dog", "cat", "bird", "fish", "cow", "horse", "pig"]
animals.sort(reverse=True)
print(animals)

#ascending order
animals = ["dog", "cat", "bird", "fish", "cow", "horse", "pig"]
animals.sort()
print(animals)


#EXERCISE TWELVE
#Using the list above, write a python program to output only animal names with the letter 
#‘a’ in them
animals = ["dog", "cat", "bird", "fish", "cow", "horse", "pig"]
for x in animals:
    if "a" in x:
        print(x)

#EXERCISE THIRTEEN
#. Write two lists, one containing your first names and the other your second names. 
# Join the two lists

first_names = ["Haulah", "Samir", "Germner", "Hoods", "Pacito"]

second_names=  ["habs","dustr","geli", "galiwa" , "Lantom"]

names = first_names + second_names
print(names)

##EXERCISE PART TWO
#Exercise a
#Consider the tuple below;
#x = (“samsung”, “iphone”, “tecno”, “redmi”)

#Write a python program to output your favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
print(x[1])

#Exercise b
#Use negative indexing to print the 2nd last item in your tuple
x=("samsung", "iphone", "tecno", "redmi")
print(x[-2])

#Exercise c
# Using the phones list above, write a python program to update “iphone” to “itel”
x = ("samsung", "iphone", "tecno", "redmi")
y = list(x)
y[1] = "itel"
x = tuple(y)
print(x)

#Exercise d
#Write a python program to add “Huawei” to your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
y = list(x)
y.append("huawei")
x = tuple(y)
print(x)


#Exercise e
#Write a python program to loop through the tuple above
x = ("samsung", "iphone", "tecno", "redmi")
for y in x:
    print(y)


#Exercise e
#. Write a python program to remove/delete the first item in your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
y = list(x)
y.pop(0)
x = tuple(y)
print(x)


#Exercise f
#Using the tuple() constructor, create a tuple of the cities in Uganda
x = ("Kampala", "Kitgum", "Alur", "Mbale")
y = tuple(x)

print(y)


#Exercise g
#Write a python program to unpack your tuple
x = ("samsung", "iphone", "tecno", "redmi")
(samsung, iphone, tecno, redmi)= x

print(samsung)
print(iphone)
print(tecno)
print(redmi)

#Exercise h
#Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above
m = ("Kampala", "Kitgum", "Alur", "Mbale")
print(m[1:4])

#Exercise i
#. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
i= ("Kampala", "Kitgum", "Alur", "Mbale")
j= ("Kamp", "Kit", "Alu", "Mba")
print(i+ j)

#Exercise j
#Create a tuple of colors and multiply it by 3
colors = ("red", "green", "blue")
print(colors*3)

#Exercise k
#Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))

#SETS(EXERCISE C)
#Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(("coffee", "tea", "milk"))
print(beverages)

#EXERCISE 2
#Use the correct method to add 2 more items to the beverages set.
beverages = set(("coffee", "tea", "milk"))
beverages.add("juice")
beverages.add("water")
print(beverages)

#EXERCISE 3 
#Given the set below;
mySet = {"oven" ,"kettle", "microwave", "refrigerator"}       
#Check if microwave is present in the set.
print("microwave" in mySet)

#EXERCISE 4
#Write a python program to remove “kettle” from the set above.
mySet = {"oven" ,"kettle", "microwave", "refrigerator"}       
mySet.remove("kettle")
print(mySet)

#EXERCISE 5
#Write a set of 4 items and a list of two items. Write a python program to add elements in 
#the list to elements in the set
mySet = {"oven" ,"kettle", "microwave", "refrigerator"}       
myList = ["kettle", "water"]
mySet.update(myList)
print(mySet)

#EXERCISE 6
#. Write two sets, one containing your ages and the other your first names. Join the two sets
ages = set((18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30))
names = set(("Haulah", "Samir", "Germner", "Hoods", "Pacito"))
print(ages.union(names))

#5. Write a python program to loop through the set above
mySet = {"oven" ,"kettle", "microwave", "refrigerator"} 
for x in mySet:
    print(x)

#EXERCISE(STRINGS)
#. Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
age = 20
txt = "My name is Mboowa, and I am {}"
print(txt.format(age))


#Exercise b
# Consider the example below;
txt = "Hello,Uganda! "
#Output the string without spaces at the beginning, in the middle and at the end at all times
print(txt.lstrip())

#3. Write a python program to convert the value of ‘txt’ to uppercase.
txt = "Hello,Uganda! "
print(txt.upper())

#4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
txt = "Hello,Uganda! "
print(txt.replace("U", "V"))


#5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.
y = "I am proudly Ugandan"
# The piece of code below will give an error when output;
x = "All “Data Scientists” are cool!"
#Write a python program to correct it.
x = "All “Data Scientists” are cool!"
print(x[1:4])

#EXERCISE (DICTIONARIES)
#1. With reference to the dictionary below, write a python program to print the value of the 
#shoe size. 
#Add this dictionary to your .py file
Shoes = {
"brand": "Nick",
"color" : "black",
"size" : 40
}
#2. Write a python program to change the value “Nick” to “Adidas”
Shoes = {
"brand" : "Nick",
"color": "black",
"size" : 40
}
Shoes["brand"] = "Adidas"
print(Shoes["brand"])



#3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes = {
"brand" : "Nick",
"color" : "black",
"size" : 40
}
Shoes["type"] = "sneakers"


#4. Write a python program to return a list of all the keys in the dictionary above.
Shoes = {
"brand" : "Nick",
"color" : "black",
"size" : 40
}
print(Shoes.keys())



#5. Write a python program to return a list of all the values in the dictionary above.
Shoes = {
"brand" : "Nick",
"color" : "black",
"size" : 40
}
print(Shoes.values())

#6. Check if the key “size” exists in the dictionary above.
Shoes = {
"brand" : "Nick",
"color" : "black",
"size" : 40
}
print("size" in Shoes)


#7. Write a python program to loop through the dictionary above.
Shoes = {
"brand" : "Nick",
"color" : "black",
"size" : 40
}
for x in Shoes:



#8. Write a python program to remove “color” from the dictionary.
 Shoes = {
"brand" : "Nick",
"color" : "black",
"size" : 40
}
Shoes.pop("color")
print(Shoes)


#9. Write a python program to empty the dictionary above.
Shoes = {
"brand": "Nick",
"color" : "black",
"size" : 40
}
Shoes.clear()


#10. Write a dictionary of your choice and make a copy of it.
dict = {
  "brand": "Benz",
  "model": "Mustang",
  "year": 1964
}
mydict = dict.copy()
print(mydict)




#11. Write a python program to show nested dictionary
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

















              

      









