# """single threading"""
# from time import sleep
# def task():
#     sleep(4)
#     print("this is from another thread")
# # task()
#
# using threading
# from time import sleep
# def task():
#     sleep(4)
#     print("this is from another thread")
# from threading import Thread
# th=Thread(target=task)
# th.start()

"""Passing arguments"""

from time import sleep
from threading import Thread
def task(sleep_time,message):
    sleep(sleep_time)
    print(message)
th=Thread(target=task,args=(1.5,"this is from thread"))
th.start()
print("waiting for the thread")
th.join()








