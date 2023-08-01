#Tuple is one of 4 built-in data types in Python used to store collections of data
#Tuples are used to store items in a single variable
#Tuples are ordered and unchangeable


phone=("samsung","tecno","iPhone")
print(phone)

#allow duplicate values

phone=("samsung","tecno","iPhone","samsung","tecno","iPhone")
print(phone)

#EXERCISE
#use the len() function with this tuple example  //6

phone=("samsung","tecno","iPhone","samsung","tecno","iPhone")
print(len(phone))

#with a different example

laptop=("dell","hp","iPad")
print(len(laptop))

#store items in the single varible in a single variable

phone=("samsung","tecno","iPhone")
laptop=("dell","hp","iPad")
print(phone)
print(laptop)

#The types of the two tuples above

phone=("samsung","tecno","iPhone")
laptop=("dell","hp","iPad")
print(type(phone))
print(type(laptop))

#immutable sequences in the tuple

phone=("samsung","tecno","iPhone")
laptop=("dell","hp","iPad")
print(phone)
print(laptop)

#EXERCISE
#how to access tuples

phone=("samsung","tecno","iPhone")

print(phone[0])
print(phone[1])
print(phone[2])

#add items to the tuple

phone=("samsung","tecno","iPhone")
z=list(phone)
z.append("Nokia")
phone=tuple(z)
print(phone)


#tupple length

phone=("samsung","tecno","iPhone","nokia")
print(len(phone))

#tuple with different data types

phone=("samsung","tecno","iPhone")
laptop=(1,2,3)
print(phone)
print(laptop)

#joining tuples
Gadgets=phone+laptop
print(Gadgets)

#checking the type of the tuple

phone=("samsung","tecno","iPhone")
laptop=(1,2,3)
print(type(phone))
print(type(laptop))


#checking the data type of the items in the tuple

phone=("samsung","tecno","iPhone")
laptop=(1,2,3)
print(type(phone[0]))
print(type(laptop[0]))


#adding items to the tuple

phone=("samsung","tecno","iPhone")
z=list(phone)
z.append("Nokia")
phone=tuple(z)
print(phone)


#add two tuples together

phone=("samsung","tecno","iPhone")
laptop=(1,2,3)
phone+=laptop
Gadgets=phone+laptop
print(phone)
print(laptop)
print(Gadgets)

 #Update Tuples according to index
x = ("kiwi", "banana", "cherry")
y = list(x)
y[1] = "berry"
x = tuple(y)

print(x)

























