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
        'ad':'Orxan',
        'soyad':'Babazade'
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
meqale=['Flask SQLAlchemy nədir və necə istifadə olunur?',
'Flask SQLAlchemy ile SQLAlchemy arasındakı fərqlər nələrdir?',
 'Flask Migration nədir və diqqət olunması lazım olan məqamla',
' Python OOP yanaşmasının ətraflı izah',
 'Python dekorator,generator nədir və istifadə yerləri',
 'Python module ve package istifadəsi ',
 'Python dunder methodlar haqqinda' ,
 'Python vasitesi ilə mini desktop tətbiqi yazmaq',
'WSGI nədir? İşləmə prinsipi necədir?',
 'Jinja template sistemi necə istifadə olunmalıdır?',
'Flask fayll'
]
added=[]
added2=[]
added3=[]
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

