#exceptional handling
    # try
	# except
	# else
	# finally

x = 5
y = "hello"
try:
	z = x + y
except TypeError:
	print("Error: cannot add an int and a str")
	

# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def divide(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
 
# Driver program to test above function
divide(9, 0)
divide(2, 2)


# Python program to demonstrate finally

# No exception Exception raised in try block
try:
	k = 6//0 #  zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('It is always executed')

	

