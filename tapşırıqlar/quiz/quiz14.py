def pangram(text):

    alph=['a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','g','q','r','s','t','u','v','w','x','y','z',]
    
    text=list(text)
    notpangram=False
    for a in alph:
        if a not in text:
            notpangram=True
            break
    if notpangram==True:
        print('not pangram')
    else:
        print('pangram')

        
    


pangram('The quick brown fox jumps over the lazy dog.')