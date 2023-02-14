"""threading"""
import threading
def coder(number):
    print("coders:",number)
    return
threads=[]
for i in range(5):
    t=threading.Thread(target=coder,args= (i,))
    threads.append(t)
    t.start()