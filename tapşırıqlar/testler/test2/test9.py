class Userpanel:
    def __init__(self):
        self.name=''
    def get_string(self):
        self.name=input('write name ')
    def print_string(self):
        print(self.name.upper())
    
u=Userpanel()
u.get_string()
u.print_string()
