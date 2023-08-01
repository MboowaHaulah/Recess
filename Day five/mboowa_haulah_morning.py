# #inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(self.name + " makes a noise")

#         class Dog(Animal):
#             def bark(self):
#                 print(self.name + " barks")

#                 def meow(self):
#                     print(self.name + " meows")

#                     #create animal objects
#                     animal=Animal("generic animal")
#                     dog=Dog("generic dog")
#                     cat=Animal("generic cat")

#                     #invoke call eat method
#                     animal.eat()
#                     dog.eat()
#                     cat.eat()

#                     #invoke call bark method
#                     animal.bark()
#                     dog.bark()
#                     cat.bark()


#                     #Exampole 2 demonstrating  inheritance

#     class Vehicle:
#         def __init__(self,brand,color):
#             self.brand=brand
#             self.color=color

#             def display(self):
#                 print ("Brand:"self.brand)
#                 print ("Color:"self.color)

#     class Car(Vehicle):
#                     def __init__(self,brand,color,wheels):
                
#                         super().__init__(brand,color)
#                         self.wheels=wheels

#                         def drive(self):
#                             super().drive()
#                             print("Car is driving")

#                             def honk(self):
#                                 super().honk()
#                                 print("Car is honk")

#                                 #create car object
#                                 car1=car("Toyota","red",4)

#                                 ##avcess( and modify car attributes
#                                 print("Brand:", car1.brand)
#                                 car1.color="blue"


#                                 #invoke car display method
#                                 car1.display()
#                                 car1.drive()
#                                 car1.honk()


                                #EXERCISE
                                #demonstrate using inheritance to calculate area and perimeter 
                                # of circle and rectangle respectively (Shape: circle)
import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating objects and calculating area/perimeter

circle = Circle(3)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

rectangle = Rectangle(5, 9)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())


#Example 3
#MULTIPLE INHERITANCE

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " makes a eating")

#         class Flyable:
#             def fly(self):
#                 print(self.name + " flies")

#                 class Bird(Animal,Flyable): #multiple inher
#                     def __init__(self, name,wings):
#                         super().__init__(name)
#                         self.species= species

#                         def display(self):
#                             super().display()
#                             print(f"Species:(self.species)")
#                             print(f"Name:(self.name)")
                            

#                             #create bird object
#                             my_bird=Bird("pigeon","bird")

# #invoke the bird methods
# my_bird.eat()
# my_bird.fly()
# my_bird.display()


#METHOD OVERIDING

class Animal:
 def  sound(self):
     print(" makes a noise")

     class Dog(Animal):
         def sound(self):
             print("barks")

             class cat(Animal):
                 def sound(self):
                     print("meows")

                     def make_sound(animal):
                         animal.make_sound()

                         #create animal objects
                         animal=Animal()
                         dog=Dog()
                         cat=Animal()

#inheritance-same method while overiding-u can use another method

#calling make_sound function
# make_sound(dog)
# make_sound(cat)
# make_sound(animal)


#POLYMORHISM
# MEHOD OVERIDING OCCURS WHEN A SUBCLASS HAS ITS OWN IMPLEMENTATION
#ALLOWS A CLASS HAVE MULTIPLE METHODS

# class Shape:
#     def calculate_area(self):
#         pass

#     Class Rectangle(Shape):

#     def__init__(self,length,width):
#     self.length = length
#     self.width = width

#     def calculate_area(self):
#         return self.width*self.length
    
#     class Circle(Shape):
#         def__init__(self,radius):
#         self.radius = radius

#         def calculate_area(self):
#             return 3.14*self.radius**2
        
#         def calculate_circumference(self):
#             return 2*3.14*self.radius
        
#         #cCREATE SHAPE OBJECTS
#         rectangle = Rectangle(5,5)
#         circle = Circle(5)

# #calculate the display area
# print ("calculating 3area: ", rectangle.calculate_area())
# print ("calculating circle area:"circle.calculate_area())


#OVERLOADING
# class Calculator:
#     def add(self, x, y):
#         return x+y
#     def add (self, x, y, z):
#         return x+y+z
#     #create object
#     calculator = Calculator()

#ABSTRACTION
#ALLOWS FOCUS ON ESSENTIAL FEATURES
# from abc import ABC,abstractclassmethod

# class Vehicle(ABC):
#  def start(self):
#     print ("Starting")

# def stop(self):
#     print("Stopping")

#     #CREATE VEHICLE OBJECT
#     car.start()
#     car.stop()

#     #truck
#     truck.start()
#     truck.stop()


#exercise2
#Demonstrate abstraction using calculating area of a circle and rectangle
import math
from abc import ABC, abstractmethod

class ShapeCalculator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(ShapeCalculator):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle(ShapeCalculator):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Example usage:
circle = Circle(3)
circle_area = circle.calculate_area()
print("The area of the circle is:", circle_area)

rectangle = Rectangle(4, 2)
rectangle_area = rectangle.calculate_area()
print("The area of the rectangle is:", rectangle_area)


#EXERCISE
#CREATE A RECEIPT PRINTING PROGRAM WITH A GUI INTERFACE
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ReceiptPrinter:
    def __init__(self, master):
        self.master = master
        master.title("Cash Receipt ")

        # Creating labels and entry fields
        self.label_receipt_number = tk.Label(master, text="Receipt Number:")
        self.label_receipt_number.grid(row=0, column=0, sticky=tk.W)
        self.entry_receipt_number = tk.Entry(master)
        self.entry_receipt_number.grid(row=0, column=1)

        self.label_received_from = tk.Label(master, text="Received From:")
        self.label_received_from.grid(row=1, column=0, sticky=tk.W)
        self.entry_received_from = tk.Entry(master)
        self.entry_received_from.grid(row=1, column=1)

        self.label_item = tk.Label(master, text="For:")
        self.label_item.grid(row=2, column=0, sticky=tk.W)
        self.entry_item = tk.Entry(master)
        self.entry_item.grid(row=2, column=1)

        self.label_price = tk.Label(master, text="Amount:")
        self.label_price.grid(row=3, column=0, sticky=tk.W)
        self.entry_price = tk.Entry(master)
        self.entry_price.grid(row=3, column=1)

        self.label_date = tk.Label(master, text="Date:")
        self.label_date.grid(row=4, column=0, sticky=tk.W)
        self.entry_date = tk.Entry(master)
        self.entry_date.grid(row=4, column=1)

        self.label_balance = tk.Label(master, text="Balance:")
        self.label_balance.grid(row=5, column=0, sticky=tk.W)
        self.entry_balance = tk.Entry(master)
        self.entry_balance.grid(row=5, column=1)

        self.label_received_by = tk.Label(master, text="Received By:")
        self.label_received_by.grid(row=6, column=0, sticky=tk.W)
        self.entry_received_by = tk.Entry(master)
        self.entry_received_by.grid(row=6, column=1)

        # Creating buttons
        self.button_add = tk.Button(master, text="Add Item", command=self.add_item)
        self.button_add.grid(row=7, column=0, columnspan=2, pady=10)

        self.button_print = tk.Button(master, text="Print Receipt", command=self.print_receipt)
        self.button_print.grid(row=8, column=0, columnspan=2, pady=10)

        # Creating text area for the receipt
        self.text_area = tk.Text(master, height=10, width=40)
        self.text_area.grid(row=9, column=0, columnspan=2)

        # Receipt counter
        self.receipt_counter = 1

    def add_item(self):
        receipt_number = self.entry_receipt_number.get()
        received_from = self.entry_received_from.get()
        item = self.entry_item.get()
        price = self.entry_price.get()

        if receipt_number and received_from and item and price:
            self.text_area.insert(tk.END, f"\nReceipt Number: {receipt_number}\n")
            self.text_area.insert(tk.END, f"Received From: {received_from}\n")
            self.text_area.insert(tk.END, f"Item: {item} - Price: ${price}\n")
            self.entry_receipt_number.delete(0, tk.END)
            self.entry_received_from.delete(0, tk.END)
            self.entry_item.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Please enter receipt number, received from, item, and price.")

    def print_receipt(self):
        receipt = self.text_area.get("1.0", tk.END)
        if receipt.strip():
            now = datetime.now()
            receipt_number = self.entry_receipt_number.get()
            date = self.entry_date.get()
            balance = self.entry_balance.get()
            received_by = self.entry_received_by.get()

            self.entry_receipt_number.delete(0, tk.END)
            self.entry_date.delete(0, tk.END)
            self.entry_balance.delete(0, tk.END)
            self.entry_received_by.delete(0, tk.END)

            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, f"Receipt Number: {receipt_number}\t\tDate: {date}\n")
            self.text_area.insert(tk.END, f"\n{receipt}\n")
            self.text_area.insert(tk.END, f"Balance: ${balance}\n")
            self.text_area.insert(tk.END, f"Received By: {received_by}\n")
            self.text_area.tag_add("center", "1.0", "2.0")
            self.text_area.tag_configure("center", justify='center')
            self.text_area.tag_add("bold", "1.0", "1.end")
            self.text_area.tag_configure("bold", font=("Helvetica", 12, "bold"))

             # Changing the text color and background color of the receipt
            self.text_area.tag_add("color", "2.0", "2.end")
            self.text_area.tag_configure("color", foreground="blue", font=("Helvetica", 14))
            self.text_area.tag_add("bg_color", "1.0", "1.end")
            self.text_area.tag_configure("bg_color", background="yellow")

        else:
            messagebox.showwarning("Error", "No items to print.")

# Creating the main Tkinter window
root = tk.Tk()
app = ReceiptPrinter(root)
root.mainloop()


