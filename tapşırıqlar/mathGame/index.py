import random

true_a=0
false_a=0
def start():
    global true_a
    global false_a
    first=random.randrange(0,9)
    second=random.randrange(0,9)
    question=input(str(first)+"+"+str(second)+"=")
    result=first+second
    question=int(question)
    
    if false_a > 9:
        print('game over'+f"| true-{str(true_a)} | false-{str(false_a)}")
    elif true_a >9:
        print('you win'+f"| true-{str(true_a)} | false-{str(false_a)}")
    else:
        if question==result:
            true_a+=1
            start()
            
        else:
            
            false_a+=1
            start()
            
     



start()
    