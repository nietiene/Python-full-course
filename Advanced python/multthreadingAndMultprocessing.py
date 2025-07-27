# multithreading means task wait a lot
# multprocessin heavy CPU task


# multithreading allow multiple task 

import threading
import time

def green(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Hello from {name}")