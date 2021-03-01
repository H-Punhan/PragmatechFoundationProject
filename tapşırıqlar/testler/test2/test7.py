class Pow:
    def  __init__(self):
        self.result=1
    def pownum(self,num1,num2):
        
        
        if num2>0:
            for a in range(0,num2):
                self.result=self.result*num1
              
          
            return self.result
        elif num2==0:
            return 0
        else:
            
            for a in range(0,abs(num2)):
                self.result=self.result*num1
               
          
            return 1/self.result
           

print(Pow().pownum(2,-1))


