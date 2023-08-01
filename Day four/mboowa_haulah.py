#create a constructor
class Human:
 def __init__(self, name,age,color):
    self.name = name
    self.age = age
    self.color = color

    #create  methods
    def eat(self):
        print("I am eating")

        def sleep(self):
            print("I am sleeping")

            def run(self):
                print("I am running")

                #create instance of a human
                human1 = Human("Haulah",20,"red")
                human1.eat()
                human1.sleep()
                human1.run()




#Example one
#car operations 
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print("The car is starting.")
        else:
            print("The car is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print("The car is stopping.")
        else:
            print("The car is already stopped.")

    def print_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


# Creating car objects
car1 = Car("Toyota", "Carolla", 2020)
car2 = Car("Ford", "Ferari", 2025)

# Starting and stopping car1
car1.start()
car1.stop()

# Starting and stopping car2
car2.start()
car2.stop()

# Printing car details
car1.print_details()
car2.print_details()




#bank account 
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} from account {self.account_number}.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")


# Creating a bank account object
account = BankAccount("123456789", 1000)

# Displaying the initial balance
account.display_balance()

# Depositing and withdrawing
account.deposit(500)
account.withdraw(200)

# Displaying the updated balance
account.display_balance()

#Example 3
#To calculate the perimeter of the rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter


# Creating a rectangle object
rectangle = Rectangle(5, 8)

# Calculating the perimeter
perimeter = rectangle.calculate_perimeter()

# Printing the result
print("Perimeter:", perimeter)


  #Example 5  
#To print student details of name,year and course
class Student:
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course

        def print_details(self):
            print(f"Name: {self.name}")
            print(f"Year: {self.year}")
            print(f"Course: {self.course}")

            #create student object
            student1 = Student("Haulah", 2020, "BSSE")
            student1.print_details()

            #display the student object
            print(student1)

#Example 6
#display results of name and age
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Hello , my name is: {self.name}")
        print(f"Hello my age is: {self.age}")


# Creating a student object
student = Student("Mboowa Haulah", 20)

# Displaying the student's information
student.display_info()

##EXERCISE
#Calculate the area and circumference of the circle
import math

class Circle:
  import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference

    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return area


# Creating a circle object
circle = Circle(7)

# Calculating the circumference and area
circumference = circle.calculate_circumference()
area = circle.calculate_area()

# Printing the results
print("Circumference:", circumference)
print("Area:", area)


#EXERCISE ONE
#calculate the area and perimeter of the rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter


# Creating a rectangle object
rectangle = Rectangle(9, 3)

# Calculating the area and perimeter
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

# Printing the results
print("Area:", area)
print("Perimeter:", perimeter)


#EXERCISE 2
#Caculate and display employee bonuses (0.5) of salary (Employee 1=15000 , Employee 2=23000)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self, bonus_percentage):
        bonus = self.salary * bonus_percentage
        return bonus

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")
        print(f"Employee Bonus: {self.calculate_bonus(0.5)}")


# Creating employee objects
employee1 = Employee("Lawan", 15000)
employee2 = Employee("Haulah", 23000)

# Displaying employee information and bonuses
employee1.display_info()
print()
employee2.display_info()
print()

#ENCAPUSULATION
#main goal is to ; hide the implementation details of the object
#protect the object from changes
#protect the object from external changes
#code organization and modularity

#with a bank account
class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} into account {self.get_account_number()}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew {amount} from account {self.get_account_number()}.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account Number: {self.get_account_number()}")
        print(f"Current Balance: {self.get_balance()}")

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance


# Creating a bank account object
account = BankAccount("123456789")

# Displaying the initial balance
account.display_balance()

# Depositing and withdrawing
account.deposit(500)
account.withdraw(200)

# Displaying the updated balance
account.display_balance()

# Accessing account number and balance using getter methods
account_number = account.get_account_number()
balance = account.get_balance()

print("Account Number:", account_number)
print("Balance:", balance)


#EXERCISE 
#Convert temperature from celcius to fahrenheit
class TemperatureConverter:
    def __init__(self, celsius):
        self.__celsius = celsius

    def convert_to_fahrenheit(self):
        fahrenheit = (self.__celsius * 9/5) + 32
        return fahrenheit

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, celsius):
        self.__celsius = celsius


# Creating a TemperatureConverter object
temperature = TemperatureConverter(37)

# Getting the Celsius temperature
celsius = temperature.get_celsius()
print("Celsius Temperature:", celsius)

# Converting Celsius to Fahrenheit
fahrenheit = temperature.convert_to_fahrenheit()
print("Fahrenheit Temperature:", fahrenheit)


#EXERCISE;Show encapsulation with employee information too give a pay increamentation
#to give a pay incrementation (Salary with employee information to new salary)
#eg from 850000 to 1000,000
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increment_salary(self, increment_amount):
        initial_salary = self.salary
        self.salary += increment_amount
        print(f"Initial salary for {self.name} was {initial_salary}.")
        print(f"Increment is {increment_amount}.")
        print(f"New salary for {self.name} is {self.salary}.")


# Create an employee instance
employee = Employee("Mboowa", 100000)

# Increment the salary by 150000
employee.increment_salary(50000)
