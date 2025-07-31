import threading

#Method-Based Thread
class MyClass:
    def show(self):
        print("Hello from class Method Thread!")

obj=MyClass()
thread1=threading.Thread(target=obj.show)
thread1.start()

#Function-Based Thread
def greet():
    print("Hello from Function Thread!")

thread2=threading.Thread(target=greet)
thread2.start()

#Class-Based Thread
class MyThread(threading.Thread):
    def run(self):  #run(self) method in class to make it thread is synataxtically required
        print("Hello from Class-Based Thread!")

thread3=MyThread()
thread3.start()
#print(MyThread)
