import threading

print("Main thread Started")
def odds():
    for i in range(1,21,2):
        print(i)
        
def evens():
    for i in range(2,21,2):
        print(i)

thread1=threading.Thread(target=odds)
thread2=threading.Thread(target=evens)

#print(thread1)
#print(thread2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Main thread Ended")
