#besinci
data=[]
id=0
class kitabevi():
    def __init__(self,ad,qiymet,yazar):
        global id
        id+=1
        self.ad=ad
        self.qiymet=qiymet
        self.yazar=yazar
        self.id=id

    def write(self):
        print(self.id,self.ad,self.qiymet,self.yazar)

kitab=kitabevi('Harry Potter',30,'Jk rowling')
kitab.write()
data.append(kitab)

kitab=kitabevi('Harry Potter',30,'Jk rowling')
kitab.write()
