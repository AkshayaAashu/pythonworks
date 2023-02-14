from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    def display(self):
        print("non abstract method")
class triangle(polygon):
    def sides(self):
        print("triangle has 3 sides")
obj=triangle()
obj.sides()
obj.display()
