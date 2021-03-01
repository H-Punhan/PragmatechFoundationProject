class possibleList:
    def __init__(self,li):
        self.li=li
        self.newlist=[]
        self.testlist=[]
    def show(self):
       
        for l in range(0,len(self.li)):
            a=self.li[l]
            self.testlist.append(a)
            if self.testlist not in self.newlist:
                self.newlist.append(self.testlist)
                self.testlist=[]
                for x in range(0,len(self.li)):
                    if self.li[l] != self.li[x]:
                        self.testlist.append(self.li[x])
                        self.testlist.append(self.li[l])
                        self.testlist.sort()
                        if self.testlist not in self.newlist:
                            self.newlist.append(self.testlist)
                        self.testlist=[]
            self.testlist=[]
                
            
        print(self.newlist)
possibleList([4,5,6,7,8,9]).show()
        