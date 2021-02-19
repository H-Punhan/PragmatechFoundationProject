import os
commands=['1-create','2-update','3-delete']

def showCommand():
    for c in commands:
        print(c)

    x=input('Run command')

    choice(x)

def choice(x):
    if x=='1':
        createFile()
    elif x=='2':
        updateFile()
    elif x=='3':
        deleteFile()

def createFile():
    file_name=input('set file name')
    f=open('layihe/backend/'+file_name+'.txt',"x")
    showCommand()

def updateFile():
    file_name=input('set file name')
    f=open('layihe/backend/'+file_name+'.txt',"w")
    w=input('write text')
    print(f.write(w))
    showCommand()

def deleteFile():

    file_name=input('set file name')
    os.remove('layihe/backend/'+file_name+'.txt')
    showCommand()

showCommand()


