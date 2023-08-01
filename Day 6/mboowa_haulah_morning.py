#REGULAR EXPRESSIONS
# []-A set of characters	"[a-m]"	
# \	Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	Any character (except newline character)	"he..o"	
# ^	Starts with	"^hello"	
# $	Ends with	"planet$"	
# *	Zero or more occurrences	"he.*o"	
# +	One or more occurrences	"he.+o"	
# ?	Zero or one occurrences	"he.?o"	
# {}Exactly the specified number of occurrences	"he.{2}o"	
# |	Either or	"falls|stays"	
# ()Capture and group	 	 

# #MATCHING AND SEARCHING
# # regex re.match() ,re.search , re.findall()

# #example 1
# #DEMONTRATING REGEX\ MATCH FIRST WORD, MATCH GROUP OF words,  MATCH ALL NUMBERS

# import re
# text="Hello,my name Haulah. I am a software developer for 2 years"
# #match first word
# print(re.match("Hello",text))

# #match group of words
# print(re.match("Haulah",text))

# #match all numbers
# print(re.match("[0-9]",text))

# #use re.findall
# print(re.findall("[0-9]",text))

# #match numbers
# import re
# match = re.findall("[0-9]",text)
# if match:
#     print(match)

#     #match white space
#     match2=re.search(r"\d+",text)
#     if match2:
#         print(match2)
    

#         match3=re.findall(r"\d+",text)
#         print(match3)
        
import re

text = "Hello, world! This is a sample text."

# Match a specific pattern
pattern = r"world"
match = re.match(pattern, text)
if match:
    print("Pattern found at the beginning of the string.")

# Search for a pattern
pattern = r"sample"
search = re.search(pattern, text)
if search:
    print("Pattern found in the string.")

# Find all occurrences of a pattern
pattern = r"is"
findall = re.findall(pattern, text)
if findall:
    print(f"Found {len(findall)} occurrences of the pattern.")

# Replace a pattern
pattern = r"Hello"
replace = re.sub(pattern, "Hi", text)
print(replace)


#EXAMPLE
import re

text = "Hello, my phone number is 123-456-7890."

# Matching a pattern
pattern = r"\d{3}-\d{3}-\d{4}"
match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())

# Finding all occurrences of a pattern
pattern = r"\b\w{5}\b"
findall = re.findall(pattern, text)
if findall:
    print("Words with 5 characters found:", findall)

# Replacing a pattern
pattern = r"\d{3}-\d{3}-\d{4}"
replace = re.sub(pattern, "XXX-XXX-XXXX", text)
print("Replaced phone number:", replace)






#validate the email address of mboowahaulah@gmail.com ormboowahaulah@gmail.123
import re
def validate_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        #explanation of the pattern used

        return True
    else:
        return False
    
    email1= "mboowahaulah@gmail.com"
    email2= "mboowah@gmail.123"

    print(validate_email(email1))
    print(validate_email(email2)) 

    #Example 2
    import re

def validate_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage:
email_address = 'mboowa@gmail.com'
if validate_email(email_address):
    print("Email is valid.")
else:
    print("Email is not valid.")


#GENERATORS AND ITERATORS
#yield
#iterator

def factorial(n):
    #return factorial of a number
    if n == 0:
        yield 1
    else:
        yield n*factorial(n-1)
    
    #print "factorial of a number 1-10
    for i in factorial(10):
        print(i)


#example 2
def factorial_generator(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result

# Example usage:
for factorial in factorial_generator(5):
    print(factorial)


#iterators
class FactorialIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1
        self.factorial = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        self.factorial *= self.current
        self.current += 1
        return self.factorial

# implementation of Factorial
factorial_iter = FactorialIterator(5)
for factorial in factorial_iter:
    print(factorial)

    #CONTENT MANAGERS
    #Content management systems (CMS) are widely used for creating and managing digital content
    #example 1
import json

def load_content():
    try:
        with open('content.json', 'r') as file:
            content = json.load(file)
    except FileNotFoundError:
        content = {}
    return content

def save_content(content):
    with open('content.json', 'w') as file:
        json.dump(content, file)

def create_content():
    title = input("Enter the title of the content: ")
    body = input("Enter the body of the content: ")

    content = load_content()
    content[title] = body
    save_content(content)
    print("Content created successfully.")

def read_content():
    content = load_content()
    if content:
        print("Available content:")
        for title, body in content.items():
            print(f"Title: {title}")
            print(f"Body: {body}\n")
    else:
        print("No content available.")

def update_content():
    title = input("Enter the title of the content to update: ")

    content = load_content()
    if title in content:
        new_body = input("Enter the new body of the content: ")
        content[title] = new_body
        save_content(content)
        print("Content updated successfully.")
    else:
        print("Content not found.")

def delete_content():
    title = input("Enter the title of the content to delete: ")

    content = load_content()
    if title in content:
        del content[title]
        save_content(content)
        print("Content deleted successfully.")
    else:
        print("Content not found.")

# Main program loop
while True:
    print("\nContent Manager Menu:")
    print("1. Create new content")
    print("2. Read existing content")
    print("3. Update existing content")
    print("4. Delete existing content")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        create_content()
    elif choice == "2":
        read_content()
    elif choice == "3":
        update_content()
    elif choice == "4":
        delete_content()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
#The main program loop provides a simple menu interface to create, read, update, or delete content.

   
   #multi threading
   #execotion of multi[le threads
   #]
import threading

def print_numbers():
    for i in range(1, 11):
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)

# Create two thread objects
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

print("Threads execution complete")

#multiprocessing
#Multiprocessing refers to the execution of multiple processes concurrently on a 
#computer system with multiple CPUs or cores
import multiprocessing

def calculate_square(number):
    result = number * number
    print(f"The square of {number} is {result}")

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    # Create a process for each number
    processes = []
    for number in numbers:
        process = multiprocessing.Process(target=calculate_square, args=(number,))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()



#DECORATORS
#to change/modify code without necessarilirily interupting the source code
  #example one
def my_decorator(func):
    def inner():
        print("Before calling the function")
    func()
    return inner

def outer_decorator():
    print("After thi outer decorator")

    outer_decorator


#example 2
def uppercase_decorator(func):
    def wrapper():
        result = func()  # Call the original function
        return result.upper()  # Modify the result
    return wrapper

@uppercase_decorator
def say_hello():
    return "Hello, world!"

print(say_hello())
