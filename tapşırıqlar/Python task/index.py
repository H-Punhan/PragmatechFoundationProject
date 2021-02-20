myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

#1
def listlen(p):
    length=0
    for m in p:
        length+=1
    print(length)
listlen(myList)


#2
def listprint(p):
    for m in p:
        print(m)

listprint(myList)

#3
def listeven(p):
    for m in p:
        if m%2==0:
            print(m)

listeven(myList)

#4
def listsort(p):
    for m in reversed(sorted(p)) :
       print(m)

listsort(myList)

#5
def listdublicate(p):
    global myList
    myList=sorted(myList)
    for m in range(len(p)):
        if myList[m] == myList[m-1]:
            print(myList[m])

listdublicate(myList)

#6
def listnoteven(p):
    for m in p:
        if m%2>0:
            myList.remove(m)

    for m in p:
        print(m)   
    
listnoteven(myList)

#7
def reverseList(p):
    for m in reversed(p):
        print(m)

reverseList(myList)

#8 
def sumList(p):
    len=0
    for m in p:
      len+=m
    print(len)
sumList(myList)

#9
def smallindex(p):
    
    p=sorted(p)
    print(p[0])

smallindex(myList)

#10
def bigindex(p):
    
    p=sorted(p)
    print(p[len(p)-1])
bigindex(myList)



