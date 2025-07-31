import threading
import time

print("Main Program Started")
def greet(name):
    print("Good Morning",name)

name="Harsh"
t1=threading.Thread(target=greet, args=(name,))
t1.start()
t1.join()

print("Both threads finished. Main Program Ends")
