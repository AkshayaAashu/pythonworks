class A:
    def read(self):
        self.x=int(input("enter the number:"))
        self.y= int(input("enter the number:"))
class B(A):
    def sum(self):
        print("sum is",self.x+self.y)
class C(A):
    def avg(self):
        print("avg is",(self.x+self.y)/2)
class D(A):
    def pro(self):
        print("product is",self.x*self.y)
obj1=B()
obj1.read()
obj1.sum()
obj2=C()
obj2.read()
obj2.avg()
obj3=D()
obj3.read()
obj3.pro()


