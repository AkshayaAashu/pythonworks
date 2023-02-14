# """NON_PARAMETARIZED CONSTRUCTOR"""
# class A:
#      def __init__(self):
#          print("Non parametrized constructor")
# obj=A()

"""PARAMETRIZED CONSTRUCTOR"""
class A:
    def __init__(self,name):
        print("parametrized constructor")

        self.n=name
    def display(self):
        print("name is:",self.n)
obj=A('anu')
obj.display()



#distructor
class A:
    def __init__(self,name):
        print("parametrized constructor")
        self.n=name
    # def __init__(self):
        print("destructor")
    def display(self):
        print("name is:",self.n)
obj=A('anu')
del obj
obj.display()
