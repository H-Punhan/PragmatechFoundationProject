myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

#1
def listlen(p):
    length=0
    for m in p:
        length+=1
    print(length)

#listlen(myList)


#2
def listprint(p):
    for m in p:
        print(m)

#listprint(myList)

#3
def listeven(p):
    for m in range(0,len(p)):
        if m%2==0:
            print(p[m])

#listeven(myList)

#4
def listsort(p):
    for m in reversed(sorted(p)) :
       print(m)

#listsort(myList)

#5
def listdublicate(p):
    p=sorted(p)
    ar=[]
    result=[]
    testindex=0
    for m in p:
        ar.append(m)

    for m in range(0,len(p)):
        for a in range(0,len(ar)):
            if p[m]==ar[a]:
                testindex+=1
                if testindex==2:
                    result.append(p[m])

        testindex=0
    print(result)

#listdublicate(myList)

#6
def listnoteven(p):
    print(myList)
    for m in range(0,len(p)):
        if m%2>0:
            p[m]='zero'
    for m in p:
        p.remove('zero')
        
    print(myList)
       
listnoteven(myList)

#7
def reverseList(p):
    for m in reversed(p):
        print(m)

#reverseList(myList)

#8 
def sumList(p):
    len=0
    for m in p:
      len+=m
    print(len)
#sumList(myList)

#9
def smallindex(p):
    
    p=sorted(p)
    print(p[0])

#smallindex(myList)

#10
def bigindex(p):
    
    p=sorted(p)
    print(p[len(p)-1])
#bigindex(myList)



