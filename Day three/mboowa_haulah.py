#OPERATORS
#Operators are used to perform operations on variables and values.
#Arithmetic operators



#Arithmetic operators
#+addition
#-subtraction
#*multiplication
#/division
#%modulus
#**exponentiation   


#Comparison operators
# == EQUAL to
# != NOT EQUAL to
# > greater than
# < less than
#>= greater than or equal to
# <= less than or equal to


#Logical operators
#logical AND 'and'
#logical OR 'or'
#logical NOT 'not'


#Assignment operators
#Assign value:'='
#add value:'+'
#add and assign value:'+='
#subtract and assign value:'-='
#multiply and assign value:'*='
#divide and assign value :/='
#modulous and assign value:'%='
#exponentiation and assign value:'**='


#Membership operators
#in -Returns True if a sequence with the 
       #specified value is present in the object	(x in y)

#not in-	Returns True if a sequence with the specified value 
            #is not present in the object (x not in y)



#Bitwise operators
#$   AND	Sets each bit to 1 if both bits are 1 eg	x & y	
#|	OR	Sets each bit to 1 if one of two bits is 1	eg x | y	
#^	XOR	Sets each bit to 1 if only one of two bits is 1 (x ^ y)	
#~	NOT	Inverts all the bits	(~x	)
#<<	Zero fill left shift	Shift left by pushing zeros in from
    # the right and let the leftmost bits fall off	x << 2	
#>>	Signed right shift	Shift right by pushing copies of the 
    #leftmost bit in from the left, and let the rightmost bits fall 
    #of f	x >> 2



#Identity operators

#is --- Returns True if both variables are the same object	(x is y	)
#is not	Returns True if both variables are not the same 
   #object	(x is not y)


#EXAMPLES OF ARITHMETIC OPERATORS
#ADDITION
x=50+45
print(x)


x = 10
y = 20

print(x + y)

#SUBTRACTION
x = 50 - 45
print(x)

#MULTIPLICATION
x = 50 * 45
print(x)

#DIVISION
x = 50 / 45
print(x)

#MODULUS

x = 50 % 45
print(x)


#EXPONENTIATION

x = 50 ** 45
print(x)

##Comparison operators
#greater than
if x < y: 
    print("x is less than y")
    print(x>y)

#less than
if x < y: 
    print("x is less than y")
    print(x<y)

#equal to
if x == y: 
    print("x is equal to y")
    print(x==y)

#greater than or equal to
if x >= y: 
    print("x is greater than or equal to y")
    print(x>=y)

#less than or equal to
if x <= y: 
    print("x is less than or equal to y")
    print(x<=y)




 ##Logical operators
#a-True
#b-false


#logical AND
print("a AND b")

#logical OR
print("a OR b")

#logical NOT 
print("a NOT b")



#Assignment operators
#Assign value:'='
k=1
print(k)

#add and assign
l=1
l+=1
print(l)

#subtract and assign
m=1
m-=1
print(m)

#multiply and assign
n=1
n*=2
print(n)

#divide and assign  
o=1
o/=2
print(o)

#modulous and assign
p=1
p%=2
print(p)

#exponentiation and assign
q=1
q**=2
print(q)


#Membership assignment operators // in and not
cars=['jeep','benz','toyota']
print(cars)

if 'jeep' in cars:
    print("jeep is in the list")
    print("benz is in the list")
    print("toyota is in the list")
    
print("jeep" in cars)
print("pusle" not in cars)


#identityoperator
#list
# is not operator

z=[1,2,3,4,5,6,7,8,9,10]
w=[ 1,2,3,4,5,6,7,8,9,10]
z=w
print(w is z)
print(w is not z)


#BIT operator
s=10
t=11

#bitwise AND operator
result=(s & t)
print(result)

#bitwise OR operator
result=(s | t)
print(result)

#bitwise XOR operator
result=(s ^ t)
print(result)

#bitwise NOT operator
result=(~s)
print(result)

#bitwise left shift operator
result=(s << 2)
print(result)

#bitwise right shift operator
result=(s >> 2)
print(result)



 #simple calculator function to add ,delete, subtract and multiply

# def calculator():
#     def add(f,g):
#         return f+g
    
#     def subtract(f,g):
#         return f-g
    
#     def multiply(f,g):
#         return f*g
    
#     def divide(f,g):
#         return f/g
    
#     def main():
#         print("Haulah is calculating")
#         number1 = float(input("Enter the first number "))
#         number2 = float(input("Enter the second number "))
#         operator=input("Enter the operator(+,-,*,/):")

# if operator == "+":
#         result=add(number1,number2)
# elif operator =='-':
#          result=subtract(number1,number2)
# elif operator =='*':
#          result=multiply(number1,number2)
# elif operator =='/':
#          result=divide(number1,number2)

# print( Add:" ,add(a,b))
# print( Subtract:" ,subtract(a,b))
# print( Multiply:" ,multiply(a,b))
# print( Divide:" ,divide(a,b))
      
      #simple calcator
def calculator():
        def add(f,g):
            return f+g
        
        def subtract(f,g):
            return f-g
        
        def multiply(f,g):
            return f*g
        
        def divide(f,g):
            return f/g
        
        def main():
            print("Haulah is calculating")
            number1 = float(input("Enter the first number "))
            number2 = float(input("Enter the second number "))
            operator=input("Enter the operator(+,-,*,/):")

# if operator == "+":
#         result=add(number1,number2)
# elif operator =='-':
#          result=subtract(number1,number2)
# elif operator =='*':
#          result=multiply(number1,number2)
# elif operator =='/':
#          result=divide(number1,number2)

# print( Add:" ,add(a,b))
# print( Subtract:" ,subtract(a,b))
# print( Multiply:" ,multiply(a,b))
# print( Divide:" ,divide(a,b))




