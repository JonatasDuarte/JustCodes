dna = str(input())
base= str(input())
cont = 0
mcont = 0
ind = 0
if(base in dna):
    for i in range(len(dna)):
        if(dna[i] == base):
            cont += 1
        else:
            cont = 0
            
        if(cont > mcont):
            mcont = cont
            ind = i
            
    print(ind-(mcont-1))
    print(mcont)
else:
    print("ERRO")