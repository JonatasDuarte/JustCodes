def risada(tx):
    vg = ['a', 'e', 'i', 'o', 'u']
    eng = False
    nova = ""
    cont =0
    for i in range(len(tx)):
        if(tx[i] in vg):
            nova += tx[i]
            cont += 1
        
    if(len(tx) > 50):
        return ("INVALIDA")
    elif(cont == 0):
        return ("INVALIDA")
    else:
        inv = nova[::-1]
        if(nova == inv):
            eng = True
        else:
            eng = False
    return eng

n = int(input())
for i in range(n):
    tx = str(input())
    fun = risada(tx)
    if(fun == True):
        print("ENGRACADA")
    elif(fun == False):
        print("SEM GRACA")
    else:
        print("INVALIDA")
                

