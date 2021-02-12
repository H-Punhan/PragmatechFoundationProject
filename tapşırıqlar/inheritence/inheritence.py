# Python da miras alma (inheritence)

class Carspec:
    def __init__(self,motor,year,color):
        self.motor=motor
        self.year=year
        self.color=color

class Car(Carspec):

    def __init__(self,motor,year,color,name):
        Carspec.__init__(self,motor,year,color)
        self.name=name

    def write(self):
        print('Car name-'+self.name + ',Car motor-'+str(self.motor) +',Car year-'+str(self.year) +',Car Color-'+self.color)

car=Car(2,2008,'black','Mercedes')
car.write()


