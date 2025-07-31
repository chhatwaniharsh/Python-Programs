import threading
import time

def natural():
    for i in range(1,27):
        print(i)
        time.sleep(1.4)
def alphabet():
    for i in range(ord("A"),ord("Z")+1):
        print(chr(i))
        time.sleep(1.45)
t1=threading.Thread(target=natural)
t2=threading.Thread(target=alphabet)
t1.start()
t2.start()

t1.join()
t2.join()
