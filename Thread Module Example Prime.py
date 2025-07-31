import threading
import time
def prime():
    for i in range(1,50):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(" P ",i)
                time.sleep(1)

def fibo():
    a=0
    b=1
    for i in range(15):
        time.sleep(1.2)
        print(" F ",a)
        a,b=b,a+b

t1=threading.Thread(target=prime)
t2=threading.Thread(target=fibo)
t1.start()
t2.start()

t1.join()
t2.join()
print("XYZ")

