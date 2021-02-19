#ucuncu
dostlar=['Ehmed','Memmed','Sabir','Qurban']
def find():
    index=0
    for d in dostlar:
        if d.find('e') != -1:
            index+=1
            print(d)
    return index
f=find()
print(f)