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
            self.testlist.append(self.li[l])
            for x in self.li:
                if x not in self.testlist:
                    self.testlist.append(x)
                    print(self.testlist)
                self.testlist=[]
        print(sorted(self.newlist))
possibleList([4,5,6,8,9]).show()
        