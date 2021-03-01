class Sumzero:
    def findsumZero(self,num,li):
        self.result=[]
        self.list=[]
        for i in range(0,len(li)):
            for x in range(0,len(li)):
               for y in range(0,len(li)):
                   if li[i]!=li[x] and li[i]+li[x]+li[y]==num:
                        self.list.append(li[i])
                        self.list.append(li[x])
                        self.list.append(li[y])
                        self.list.sort()
                        if self.list not in self.result:
                            self.result.append(self.list)
                   self.list=[]
        print(self.result)
        
            
Sumzero().findsumZero(0,[-25, -10, -7, -3, 2, 4, 8, 10])

      
        