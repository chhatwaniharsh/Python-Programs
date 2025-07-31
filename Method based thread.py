import threading

class MyClass:
    def show(self):
        print("Hello from class Method Thread!")

obj=MyClass()
thread1=threading.Thread(target=obj.show)
thread1.start()
