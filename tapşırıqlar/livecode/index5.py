#besinci
id=0
class kitabevi():
    def __init__(self,ad,qiymet,yazar):
        self.ad=ad
        self.qiymet=qiymet
        self.yazar=yazar
    

    def write(self):
        print(self.ad,self.qiymet,self.yazar)

kitab=kitabevi('Harry Potter',30,'Jk rowling')
kitab.write()
