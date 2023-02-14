n=int(input("enter the number:"))
for i in range(n):
    for s in range(0,i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end=" ")
    print()

