#adding elements in to a list using function

num=int(input("enter the no.of elements to be added to the list:"))
list1=[]
def list(n):
    for i in range(num):
        item=int(input("enter the numbers:"))
        list1.append(item)
    print(list1)
list(num)