# iterator  uzerinde geze bileceyimiz bir obyektdir.Eyer bir obyekte iterator elave oluna bilirse 
# bu obyekt iterable oyekt deyilir listler ve dict ler kimi 
array=[1,2,3,4,5]
dictar={
    'name':"punhan",
    'surname':"huseynov",
    'age':19
}

for a in array:
    print(a)

for a in dictar:
    print(dictar[a])

# Lakin class obyektlerine de iterator elave edile biler

class customArray:

    def __init__(self,array):
        self.index=-1
        self.array=array

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index+=1
        if self.index<len(self.array):
            return self.array[self.index]
        else:
            self.index=-1
            raise StopIteration

        
    
c=customArray([1,1,1,1]) 
for a in c:
    print(a)
    
    
        
        
