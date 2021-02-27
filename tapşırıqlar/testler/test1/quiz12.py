def palindrome(word):
    
    reversedlist=list(word)
    reversedlist.reverse()
    newword=''
    for r in reversedlist:
        newword+=r
        
    if word==newword:
        print(' palindrome')
    else:
        print('not palindrome')
     
    
palindrome('tenet')
