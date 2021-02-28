class Intnumreal:
    
    def __init__(self):
        self.roman=[
            {
                'rnum':'I',
                'num':1
            }
            ,
            {
                'rnum':'V',
                'num':5
            }
            ,
            {
                'rnum':'X',
                'num':10
            }
            ,
            {
                "rnum":'L',
                'num':50
            }
            ]
    def inttoRomannum(self,num):
        self.num=num
        self.result=''
        for i in self.num:
            for m in range(0,len(self.roman)):
                if int(i)==self.roman[m]['num']:
                    self.result+=self.roman[m]['rnum'] 

        print(self.result)
            
newint=Intnumreal().inttoRomannum([14])

    