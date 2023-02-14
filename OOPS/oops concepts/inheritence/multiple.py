class A:
    def emp(self):
        self.name=input("enter the name:")
        self.age=int(input("enter the age:"))
class B:
    def salary(self):
        self.sal=int(input("enter the salary:"))
class C(A,B):
    def details(self):
        print("name is",self.name)
        print("age is",self.age)
        print("salary is",self.sal)


obj=C()
obj.emp()
obj.salary()
obj.details()
