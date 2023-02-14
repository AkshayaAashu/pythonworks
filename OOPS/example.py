
class Emp:
    def display(self):
        print("simple function")
obj=Emp()
obj.display()


class Emp:
    x=100

    def display(self):
        print("simple function")
obj=Emp()
obj.display()
print("value of x is",obj.x)


class Emp:
    x=100
    def display(self):
        print("simple function")
    def disp():
        print("without self parameter")
obj=Emp()
obj.display()
print("value of x is",obj.x)
ob=Emp
ob.disp()


class Emp:
    x=100
    def display(self):
        print("simple function")
    def sum(self):
        print("sum is",30+40)

obj=Emp()
obj.display()
print("value of x is",obj.x)
obj.sum()


class Emp:
    x=100
    def display(self):
        print("simple function")
    def sum(self):
        print("sum is",30+40)

obj=Emp()
obj.display()
print("value of x is",obj.x)
obj.sum()



class Emp:
    x=100
    def display(self):
        print("simple function")
    def sum(self):
        print("sum is",30+40)

obj=Emp()
obj.display()
print("value of x is",obj.x)
obj.sum()


class Emp:
    x=100
    def display(self):
        print("simple function")
    def sum(self,a,b):
        print("sum is",30+40)
    def product(se,a,b):
        print("product is",a*b)

obj=Emp()
obj.display()
obj.sum(30,40)
obj.product(3,4)


#4
class Emp:
    def read(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print("sum is:",self.a+self.b)
    def product(c):
        print("product is:",c.a*c.b)

obj=Emp()
obj.read(10,20)
obj.sum()
obj.product()


"""factorial"""
class Emp:
    def fact(sl,x):
        if x==1:
            return 1
        else:
            return x*sl.fact(x-1)
obj=Emp()
n=int(input("enter the number:"))
f=obj.fact(n)
print("factorial is:",f)






