import threading
import time


sem = threading.Semaphore()
print("MultiThreading using Semaphore!!")
def fun1():
    while True:
        sem.acquire()
        print("Function 1")
        sem.release()
        time.sleep(0.25)
        

def fun2():
    while True:
        sem.acquire()
        print("Function 2")
        sem.release()
        time.sleep(0.25)
        

t1 = threading.Thread(target = fun1)
t1.start()

t2 = threading.Thread(target = fun2)
t2.start()