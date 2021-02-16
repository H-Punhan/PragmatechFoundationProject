n=int(input('Bir reqem yazin'))

def result(x):
    #Burda verilən dəyər  neçə olursa olsuna  əyər təkdir-sə  cavab yenədə  weird olacaq
    if x%2>0:
        print('weird')
    elif x>2 and n<5 and x%2==0:
        print('not weird')

    elif x>6 and n<20 and x%2==0:
        print('weird')
    
    elif x>20  and x%2==0:
        print('Not weird')
    
   

result(n)