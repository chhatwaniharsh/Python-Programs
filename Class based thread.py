import threading

class MyThread(threading.Thread):
    def run(self):
        print("Hello from Class-Based Thread!")

thread1=MyThread()
thread1.start()
