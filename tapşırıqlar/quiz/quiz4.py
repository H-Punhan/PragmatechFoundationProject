
def reversString(text):
    li=list(text)
    newt=''
    for l in reversed(li):
        newt+=l
    print(newt)
    
reversString('1234abcd')
    