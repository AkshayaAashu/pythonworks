import time
import threading
def cal_square(num):
    print("calculate the square root of the given number")
    for n in num:
        time.sleep(0.3)
        print("square is:",n*n)
def cal_cube(num):
    print("calculate the cube of the given number")
    for n in num:
        time.sleep(0.5)
        print("cube is:",n*n*n)
arr=[4,5,6,7,3]
t1=time.time()
th1=threading.Thread(target=cal_square, args=(arr,))
th2=threading.Thread(target=cal_cube, args=(arr,))
th1.start()
th2.start()
th1.join()
th2.join()
print("total time take"
      "n by threads is:",time.time()-t1)