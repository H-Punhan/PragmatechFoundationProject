
def perfectnumber(pernum):
    result=0
    for p in range(1,pernum):
        if pernum%p==0:
             result+=p
        
    if result==pernum:
        print('perfect')
    else:print('not perfect')   

perfectnumber(496)