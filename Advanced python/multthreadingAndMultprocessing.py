# multithreading means task wait a lot
# multprocessin heavy CPU task


# multithreading allow multiple task 

import threading
import time

def greet(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Hello from {name}")

# create threads
t1 = threading.Thread(target=greet, args=("Thread 1"))   
t2 = threading.Thread(target=greet, args=("Thread 2"))   

# Start threads

t1.start()
t2.start()

