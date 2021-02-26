reqem=[3,56,78,12,56,25]
def forfunc(exp):
    for a in reqem:
        if exp(a):
            print(a)


#forfunc(lambda x:x%5==0)
#forfunc(lambda x:x>9)
#forfunc(lambda x:int(list(str(x))[0])+int(list(str(x))[0])>10)

#------------------------------------

isciler=[
    {
        'ad':'Memmed',
        'maas':'600AZN'
    },
    {
        'ad':'Cemile',
        'maas':'500AZN'
    },
    {
        'ad':'Saleh',
        'maas':'1200AZN'
    },
    {
        'ad':'Gulnar',
        'maas':'980AZN'
    }
]

# iscilerin maas cemini tapin
# iscilerin %18 faiz vergi cixildidan sonra galan maaslarini list halinda cap edin
# maasi ortlama maasdan yuksek olan iscilerin siyahini list olaraq cap edin


def sumSalary(lis):
    maaslar=[]
    maas=""
    for l in lis:
        maas=''
        l=list(l['maas'])
        for m in l:
            if m.isnumeric()==True:
                maas+=m

        maaslar.append(int(maas))
    return maaslar
print(sum(sumSalary(isciler)))

def percent():
    maaslar=[]
    for i in sumSalary(isciler):
        i=i-(0.18*i)
        maaslar.append(int(i))

    return  maaslar

print(percent())

def findEmploye(lis):
    newlist=[]
    maas=''
    for i in range(0,len(lis)):
        maas=''
        x=list(lis[i]['maas'])
        for m in x:
            if m.isnumeric()==True:
                maas+=m
        
        isciler[i]['maas']=int(maas)
        if isciler[i]['maas']>500:
            newlist.append(isciler[i])
    
    return newlist
print(findEmploye(isciler))



    




    








