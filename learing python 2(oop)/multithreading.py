#multithreading (multitasking) --> good for I/O bound tasks like reading file or featching data from APIs
# threading.Thread(target=my_function)

import threading
import time

#suppose we have multiple tasks for today

def meet (first, last):
    time.sleep(4)                     #this means it takes 4 second to do thhis task
    print(f"Meet {first} {last}")

def go (where):
    time.sleep(6)
    print (f"went to {where}")

def eat():
    time.sleep(2)
    print (f"eating completed")

task1 = threading.Thread(target = meet, args=("tirthankar", 'katiwada'))      #this line makes meet() a part of multi thread
task1.start()                                                                #this line calls the meet() function

task2 = threading.Thread(target = go, args=("AR bug Hunt",))        #that comma is necessary as it symbolizes a tuple. With it it will me a string which is wrong syntax
task2.start()

task3 = threading.Thread(target = eat)
task3.start()

task1.join()              #these lines make sure that the code only goes further down after completion of these tasks       
task2.join()
task3.join()


print("your tasks for today are completed")



