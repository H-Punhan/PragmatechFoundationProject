class Rectsize:
    def __init__(self,w,h):
        self.width=w
        self.height=h
    def getsize(self):
        return self.width*self.height
    
print(Rectsize(100,5).getsize())