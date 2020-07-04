matrix=[]
soma = 0
somadia=0
pos = 0
menor = 9999999999
delta = 0
for i in range(3):
    linha=[]
    for j in range(3):
        val = int(input())
        if(menor>val):
            menor = val
        if(val > 0):
            soma += val
            pos += 1
        if(i != j):
            somadia += val
        linha.append(val)
    matrix.append(linha)
    
if(menor%2 == 0): delta = 1
else: delta = 0

print("%.2f"%(soma/pos)+" "+str(menor)+" "+str(delta)+" "+str(somadia))