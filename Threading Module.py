import threading

def numbers():
    for i in range(1,27):
        print(i)
        
def alphabets():
    for i in range(ord('A'), ord('Z') + 1):
        print(chr(i))

t1=threading.Thread(target=numbers)
t2=threading.Thread(target=alphabets)
t1.start()
t2.start()
