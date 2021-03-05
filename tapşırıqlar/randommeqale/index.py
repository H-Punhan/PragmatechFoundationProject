import random
foundation11=[
    {
        'ad':'Punhan',
        'soyad':'Huseynov'
    },
    {
        'ad':'Jale',
        'soyad':'Mirzeyeva'
    },
    {
        'ad':'Huseyn',
        'soyad':'Ehmedzade'
    },
    {
        'ad':'Orxan',
        'soyad':'Babazade'
    },
    {
        'ad':'Ibrahim',
        'soyad':'Huseynov'
    },
    {
        'ad':'Orxan',
        'soyad':'Mustafayev'
    },
     {
        'ad':'Fatime',
        'soyad':'Yaqubova'
    },
     {
        'ad':'Ferid',
        'soyad':'Kerimli'
    },
    {
        'ad':'Togrul',
        'soyad':'Merdanov'
    },
     {
        'ad':'Nicat',
        'soyad':'Qurbani'
    },
     {
        'ad':'Nagi',
        'soyad':'Eliyev'
    },
    {
        'ad':'Elmir',
        'soyad':'Sefereliyev'
    },
     {
        'ad':'Elcan',
        'soyad':'Quliyev'
    },
     {
        'ad':'Mehemmed',
        'soyad':'Sadiqzade'
    }
]
meqale=['OOP nedir ?',
'Modul nedir ?','Class nedir ?' ,'Inheritence nedir ?','Polymorphmism nedir ?',
'Encapsulation nedir','Return nedir ?','Interpreter nedir ?','Compiler nedir ?',
'Constructor nedir ?','Metod nedir ?','Decarator nedir ?','Virtual enviroment nedir ?','Package nedir ?']
added=[]
added2=[]

def meqaleelaveet(f,m):
    
    
    
    for i in f:
        r=m[random.randrange(0,len(m))]
        if  r not in added2:
            o={'ad':i['ad'],
            "soyad":i['soyad'],
            "meqale":r}
            o2={'ad':i['ad'],
            "soyad":i['soyad']
            }
            if o2 not in added3:
                
                added3.append(o2)
                added.append(o)
                added2.append(r)
            else:pass
            

           
        
    if len(added2)!=len(m):
        meqaleelaveet(f,m)
    else:
        
        for i in added:
            print(f"{i['ad']} {i['soyad']}-{i['meqale']}")
        
    

    
    
meqaleelaveet(foundation11,meqale)

