#Set is one of 4 built-in data types in Python used to store collections of data
#Sets store multiple items in a single variable{}
#unchangeable although one can add and remove 


foodset={"cassava","potato","yam"}
print(foodset)

#Duplicates in the sets //aint allowed

foodset={"cassava","potato","yam","yam","yam"}
print(foodset)

#EXERCISE
#find the length of your set

foodset={"cassava","potato","yam"}
print(len(foodset))

#datatype of the set

foodset={"cassava","potato","yam"}
print(type(foodset))

#accessing items in the set

#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, 
#or ask if a specified value is present in a set,
#by using the in keyword.

phone={"samsung","tecno","iPhone"}
for x in phone:
  print(x)


#check if tecno is present in

phone={"samsung","tecno","iPhone"}

print("tecno" in phone)

#or
if "tecno" in phone:
  print("tecno is present")
else:
  print("tecno is not present")

#add two sets together for phone and foodset

phone={"samsung","tecno","iPhone"}
foodset={"cassava","potato","yam"}

phone.update(foodset)
print(phone)

#add an item in the set

phone={"samsung","tecno","iPhone"}
phone.add("nokia")
print(phone)

#remove an item from the set

phone={"samsung","tecno","iPhone","nokia"}
phone.remove("nokia")
print(phone)

