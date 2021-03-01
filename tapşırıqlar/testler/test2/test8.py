class Reverseword:
    def reverse(self,word):
        self.word=word.split()
        self.word.reverse()
        self.list=[]
        for i in self.word:
            self.list.append(i)
        self.word=''
        for l in range(0,len(self.list)):
            self.word+=self.list[l]
            self.word+=' '
        return self.word

print(Reverseword().reverse('hello .py'))