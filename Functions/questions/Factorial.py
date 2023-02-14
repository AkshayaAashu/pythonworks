#factorial of a number using function with return type and function parameter
num=int(input("enter the number:"))
def factorial(n):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
f=factorial(num)
print("factorial is ",f)