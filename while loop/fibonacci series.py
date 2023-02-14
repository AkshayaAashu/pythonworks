n=int(input("Enter number:"))
a=0
b=1
sum=0
while(a<=n):
    sum=a+b
    print(a)
    a=b
    b=sum
    #print(a)