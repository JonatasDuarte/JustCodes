frase = str(input())
cont = 0
for i in range(len(frase)):
        if(frase[i] == " " and frase[i+1] == " "):
            cont += 0
        elif(frase[i] == " "):
            cont += 1
print(cont + 1)
    
    
