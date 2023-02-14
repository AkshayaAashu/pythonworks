class A:
    def read(self):
        self.x=int(input("enter the number:"))
        self.y=int(input("enter the number:"))
class B(A):
    def sum(self):
        self.s=self.x+self.y
        print("sum is",self.s)
class C(B):
    def avg(self):
        print("avg is",self.s/2)

obj=C()
obj.read()
obj.sum()
obj.avg()