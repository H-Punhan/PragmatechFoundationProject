class Circle:
    def __init__(self,radius):
        self.radius=radius
    def getarea(self):
        return 3.14*(self.radius*self.radius)
    def getperimeter(self):
        return 3.14*(self.radius*2)
        
    

print(Circle(5).getperimeter())
print(Circle(5).getarea())