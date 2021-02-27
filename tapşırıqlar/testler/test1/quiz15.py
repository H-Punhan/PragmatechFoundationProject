text='green-red-yellow-black-white'

def splitWord(te):
    newtext=''
    te=te.split('-')
    te=sorted(te)
    linevalue=len(te)-1
  
    for t in range(0,len(te)+linevalue):
        if t%2>0:
            te.insert(t,'-')
            
        newtext+=te[t]
    print(newtext)

        


splitWord(text)
