"""print even and odd numbers between 1 to the entered number"""

n=int(input("enter the number:"))
i=1
while i<=n:
    print(i)
    if (i%2==0):
        print("even number")
    else:
        print("odd number")
    i=i+1