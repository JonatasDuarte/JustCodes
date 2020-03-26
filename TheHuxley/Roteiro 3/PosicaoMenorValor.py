n = int(input())
cont = 0
menor = []
posi = 0
na = 0
ent = input().split()
l = [int (i) for i in ent]

for i in range(n):
    cont += 1
    
    if(na == 0):
        menor = l[0]
        na += 1
        
    if(menor > l[i]):
        menor = l[i]
        posi = cont

print("Menor valor:", menor)
if(posi == 0):
    print("Posicao:", posi)
else:
    print("Posicao:", posi-1)