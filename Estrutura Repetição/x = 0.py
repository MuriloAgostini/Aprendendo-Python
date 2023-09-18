achou = False 
i = 0 
frase = ("Ao infinito e além!")
x=0
while (not achou) and (i < len(frase)): 
    
    x+=1
    print(x)
    if i % 2 == 0: 
        i += 1 
        continue 
 
    if frase[i] == ' ': 
        achou = True 
 
    i += 1 