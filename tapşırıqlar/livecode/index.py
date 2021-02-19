# birinci
def hesabla():
    x=input('birinci eded')
    b=input('ikinci eded')
    c=int(x)+int(b)
    return c/2
#a=hesabla()
#print(a)
#ikinci
def  userp():
    name=input('username')
    passw=input('password')
    if name=='admin' and passw=='123456':
        print('duzdur')

    else:print('sefdir')
#userp()

dostlar=['Ehmed','Memmed','Sabir','Qurban']

def find():
    index=0
    for d in dostlar:
        if d.find('e') != -1:
            index+=1
    return index
f=find()
print(f)

def hesabla2():
    meqale="Baş nazir bildirib ki, müxtəlif sahələrdə əməkdaşlığımızı nəzərdə tutan bir çox sənədlər dünən keçirilən görüşlərdə imzalanıb: “Bu, çoxtərəfli platforma gələcək üçün böyük perspektivlər vəd edir. Əminəm ki, bu gün keçirilən iclasın nəticələri ikitərəfli münasibətlərin inkişafına da təkan verəcək. Prezident İlham Əliyev və Rəcəb Tayyib Ərdoğanın yorulmaz səyləri nəticəsində ölkələrimiz arasında münasibətlər ən yüksək səviyyəyə çatıb. Əməkdaşlığımız bütün sahələri əhatə edir. 2023-cü ilədək ticarət dövriyyəmizi 15 milyard dollara çatdırmaq əsas hədəflərimizdəndir”."
    print(len(meqale))
hesabla2()
class kitabevi():
    def __init__(self,ad,qiymet,yazar):
        self.ad=ad
        self.qiymet=qiymet
        self.yazar=yazar

    def write(self):
        print(self.ad,self.qiymet,self.yazar)

kitab=kitabevi('Harry Potter',30,'Jk rowling')
kitab.write()