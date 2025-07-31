import threading

def greet():
    print("Hello from Function Thread!")

thread1=threading.Thread(target=greet)
thread1.start()

