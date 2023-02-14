
class A:
    var1=None #public data member
    _var2=None #protected data member
    __var3=None #private data menber

#constructor
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3

    def displayPublicMembers(self): #public member function
        print("public data member:",self.var1) #accessing public datamember
    def _displayProtectedMember(self):
        print("protected data member:",self._var2)
    def __displayPrivateMembers(self):
        print("private data member:",self.__var3)

    def accessPrivateMembers(self):
        self.__displayPrivateMembers() #accessing private memberfunction

    #derived class
class B(A):
    def __init__(self,var1,var2,var3): #constructor
        A.__init__(self,var1,var2,var3)

    def accessProtectedMembers(self):#accessing protected me
        self._displayProtectedMember()

#creating objects of the derived class
obj=B("Pub_red","Pro_white","Private_green")
#calling public member function of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()
#obj.accessprivate member
#object can aacess public member
print("object is accessing public member:",obj.var1)
print("object is accessing protected member:",obj._var2)
#object cannot access private member,so it will generate attribute error
#print(obj.__var3)
print(obj._A__var3) #accessing name mangled variables

#name mangling
#A process in which any given identifier with one trailing underscore and two leading underscore
#is textually
