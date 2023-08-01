#a)Show a context manager for file handling that automatically opens and closes a file
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# implementation
with FileHandler('myfile.txt', 'r') as f:
    contents = f.read()
    



#EXERCISE B
# Shows a context manager for managing a database connection.
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

with DatabaseConnection('mydatabase.db') as conn:
    cursor = conn.cursor()
    #cursor.execute("SELECT * FROM mydatabase")
    rows = cursor.fetchall()
    

#EXERCISE 3
#c)Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.
import threading
import multiprocessing
import time

def my_function(duration):
    print(f"Starting my_function for {duration} seconds")
    time.sleep(duration)
    print(f"Finished my_function for {duration} seconds")

if __name__ == '__main__':
    # Multithreading example
    thread1 = threading.Thread(target=my_function, args=(4,))
    thread2 = threading.Thread(target=my_function, args=(8,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    # Multiprocessing 
    multiprocessing.freeze_support()
    process1 = multiprocessing.Process(target=my_function, args=(4,))
    process2 = multiprocessing.Process(target=my_function, args=(8,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
