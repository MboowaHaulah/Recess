#input and output in python
#input('prompt')


#eg of input

# name= input("Enter name:")
# print ("My name is,"+name)

#EXAMPLE 2
# number=int(input("Enter a value" ))
# product = number*10
# print(product)


# #MULTIPLY INPUTS IN PYTHON
# s,r,w=map(int,input("Enter values:").split())
# print("The valuers are :",end=" ")
# print(s,r,w)

#how to capture input from a tuple
# w=(2,3,4,5,6,8)
# print("The current tuple")
# print(w)

# E = list(w)
# E.append(int(input("Enter new value: ")))

# w=tuple(E)
# print("The updated tuple")
# print(w)

myList = list(map(int,input("Enter list values: ").split))
mySet = set(map(int,input("Enter set values: ").split))
print(myList)
print(mySet)
