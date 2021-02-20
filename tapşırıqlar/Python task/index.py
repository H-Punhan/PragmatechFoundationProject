myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

#1
def listlen():
    print(len(myList))
listlen()

#2
def listprint():
    for m in myList:
        print(m)

listprint()

#3
def listeven():
    for m in myList:
        if m%2==0:
            print(m)

listeven()

#4
def listsort():
    for m in reversed(sorted(myList)) :
       print(m)

listsort()

#5
def listdublicate():
    global myList
    myList=sorted(myList)
    for m in range(len(myList)-1):
        if myList[m] == myList[m-1]:
            print(myList[m])

listdublicate()

#6
def listnoteven():
    for m in myList:
        if m%2>0:
            myList.remove(m)

    for m in myList:
        print(m)   
    
listnoteven()

#7
def reverseList():
    for m in reversed(myList):
        print(m)

reverseList()

#8 
def sumList():
    print(sum(myList))

sumList()

#9
def smallindex():
    global myList
    myList=sorted(myList)
    print(myList[0])

smallindex()

#10
def bigindex():
    global myList
    myList=sorted(myList)
    print(myList[len(myList)-1])
bigindex()