n = int(input())
l = []
posi = 0
cont = 0
for i in range(n):
    l.append(int(input()))

valor = int(input())

if(len(l) == 0):
    cont += 1
    print("[ ]")
    print("A lista estah vazia - nao eh possivel remover elemento")

for i in range(len(l)):
    if(l[i] == valor):
        cont += 1
        posi = i
        print("[",end=" ")        
        for j in range(len(l)):
            print(l[j],end=" ")
        print("]")
        l = l[:(posi)] + l[(posi+1):]
        print("[",end=" ")        
        for j in range(len(l)):
            print(l[j],end=" ")
        print("]")
        break

if(cont < 1):
    print("[",end=" ")        
    for j in range(len(l)):
        print(l[j],end=" ")
    print("]")
    print("Nao eh possivel remover o elemento",valor)


        
