"""function overloading"""
class A:
    def display(self,name=None):
        if name is None:
            print("hello")
        else:
            print("hello "+name)
obj=A()
obj.display()
obj.display("anu")

"""function overiding"""

class rectangle:
    def area(self,l,b):
        print("area of rectangle:",l*b)
class square(rectangle):
    def area(self,l,b):
        print("area of square is:",l*b)


obj=square()
obj.area(20,20)