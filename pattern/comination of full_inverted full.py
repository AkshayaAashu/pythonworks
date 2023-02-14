n=int(input("enter the rows:"))
for i in range(n):
    for s in range(0,i):
        print(" ",end=" ")
    for j in range(n-i):
        print(" * ",end=" ")
    print()

for i in range(n):
    for s in range(n-i):
        print("  ",end=" ")
    for j in range(i+1):
        print(" * ",end=" ")
    print()