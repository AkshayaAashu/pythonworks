class A:
    def displayA(self):
        print("base class method")
class B(A):
    def displayB(self):
        print("derive class method")
obj=B()
obj.displayA()
obj.displayB()

"""SUM OF TWO NUMBERS"""
class A:
    def read(self):
        self.x=int(input("enter the number:"))
        self.y=int(input("enter the number:"))
class B(A):
    def sum(self):
        print("sum is",self.x+self.y)
obj=B()
obj.read()
obj.sum()
