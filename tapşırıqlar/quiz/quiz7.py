
text='The quick Brow Fox'

def upperLower(te):
    lower=0
    upper=0
    te=list(te.strip())
    for t in te:
        if t.isupper() == True:
            upper+=1
            
        else:
            lower+=1
            
        
    print(upper,lower)

upperLower(text)
