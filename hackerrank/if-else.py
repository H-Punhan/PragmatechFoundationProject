n=int(input('Bir reqem yazin'))

def result(x):
    #Burda verilən dəyər  neçə olursa olsuna  əyər təkdir-sə  cavab yenədə  weird olacaq
    if x%2>0:
        print('Weird')
    elif x>2 and x<5 and x%2==0:
        print('Not weird')

    elif x>6 and x<20 and x%2==0:
        print('Weird')
    
    elif x>20  and x%2==0:
        print('Not weird')
    
   

result(n)