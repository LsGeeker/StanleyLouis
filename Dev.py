import random
import time

tab = ['___',"|","+"]



lim = 40
while True:
    choix = random.choice(tab)
    obj = [" " for _ in range(0 ,lim-1)]
    
    aff = " "*lim
    
    post = random.randint(0, lim-1)
    
    while post < lim:
        print("\n" *20)
        
        aff = aff[:post ] + choix + aff[post + 1:]
        
        print(aff)
        post +=1
        
        time.sleep(1)              
    
    

