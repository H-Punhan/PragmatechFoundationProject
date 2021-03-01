class Findsumindex:
    def find(self,num,li):
        self.testlist=[]
        self.result=[]
        
        
        for i in range(0,len(li)):
            for x in range(0,len(li)):
                if li[i]+li[x]==num and x!=i:
                    if i and x not in self.result:
                        self.testlist.append(i)
                        self.testlist.append(x)
                        self.testlist=sorted(self.testlist)
                        if self.testlist not in self.result:
                            self.result.append(self.testlist)
                    self.testlist=[]
    
          
        return self.result
        
print(Findsumindex().find( 70,[10,20,10,40,50,60,70]))
