
def unigueList():
    li1=[1,2,3,3,3,3,4,5,5,5,5]
    li2=[]
    for l in li1:
        if l not in li2:
            li2.append(l)
    print(li2)
unigueList()