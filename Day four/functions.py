#Group blocks of code 
#There is need for clean code , reusable,maintainable code
#ie def function_name():

def afternoon():
    print ("class starts")
    print("close to 100")

#calling a function
afternoon()

#parameters and arguments
#calling a function
def afternoon(first_name, last_name):
    print (f"Hi {first_name}, {last_name}")
    print("I hate studying")

    #calling a function
    afternoon("Haler","Mboowa");

#Example
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#function to take in more arguments
def my_function(x, y):
  return 5 * x + y

print(my_function(3, 5))
print(my_function(5, 9))
print(my_function(9, 3))

#many arguments using *args
def my_function(*args):
  return sum(args)

print(my_function(1, 2, 3, 4, 5))
print(my_function(1, 2, 3, 4, 5, 6, 7, 8, 9))