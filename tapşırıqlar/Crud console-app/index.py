
id=0
class Users:
    def __init__(self,ad,soyad,id):
        self.ad=ad,
        self.soyad=soyad
        self.id=str(id)
    def showUser(self):

        print(f"{self.id}| {self.ad} | {self.soyad}")
        



users=[]

commandList=[
    "1. Yeni istifadəçi əlavə et ",
    "2. Bütün istifadəçilər",
    "3. Seçilən istifadəçini sil",
    "4. Seçilən istifadəçinin məlumatlarını dəyişdir",
    "5. Əsas menunu göstər"
]

def showCommand():
    for c in commandList:
        print(c)
    x=input(' Yonlendirme ucun bir reqeme basin ')
    
    choice(x)


def choice(x):
    if x=='1':
        addUser()
    elif x=='2':
        showUsers()
    elif x=='3':
        delUsers()
    elif x=='4':
        updateUser()
    elif x=='5':
        showCommand()

# add user
def addUser():
    global id
    id+=1
    ad=input('Adiniz ')
    soyad=input('Soyadiniz ')
    u=Users(ad,soyad,id)
    users.append(u)
    showCommand()

#delete user
def showUsers():

    for u in users:
        u.showUser()
    showCommand()

# delete user
def delUsers():
    x=input('Silmek istediyiniz istifadecinin id sini yazin ')
    for u in users:
        if u.id==x:
            users.remove(u)
            print('silindi')
            showCommand()
    

#update user
def updateUser():
    x=input('Update etmek ucun istiadecinin id-sini yazin')
    
    for u in users:
        if u.id==x:
            yeniAd=input('Yeni adi yazin-')
            yeniSoyad=input('yeni soyad yazin-')
            u.ad=yeniAd
            u.soyad=yeniSoyad

    showCommand()

showCommand()