reqem=[3,56,78,12,56,25]
def forfunc(exp):
    for a in reqem:
        if exp(a):
            print(a)


forfunc(lambda x:x%5==0)
forfunc(lambda x:x>9)
forfunc(lambda x:int(list(str(x))[0])+int(list(str(x))[0])>10)


# isciler=[
#     {
#         'ad':'Memmed',
#         'maas':'600AZN'
#     },
#     {
#         'ad':'Cemile',
#         'maas':'500AZN'
#     },
#     {
#         'ad':'Saleh',
#         'maas':'1200AZN'
#     },
#     {
#         'ad':'Gulnar',
#         'maas':'980AZN'
#     }
# ]

# maaslar=['600AZN','500AZN','1200AZN','980AZN']
# maas2=[]

# def findnumber():
#     maas=''
#     for m in maaslar:
  
#         m=list(m)
        
#         for m1 in m:
        
#              if m1.isnumeric()==True:
#                  maas+=str(m1)
        

#         maas2.append(int(maas))
#         maas=''
#     print(maas2)

# findnumber()






