class Rectangle:
    def __init__(self,l,b):
        self.length = l 
        self.breadth = b 
    def area(self):
        return self.length*self.breadth

class Cuboid(Rectangle):
    def __init__(self,l,b,h):
        self.height = h 
        super().__init__(l,b)
    
    def volume(self):
        return self.length*self.breadth*self.height

c = Cuboid(1,2,12)
print(c.volume())
    
        