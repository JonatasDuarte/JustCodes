n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

posi = int(input())


if(len(l) == 0):
    print("[ ]")
    print("A lista estah vazia - nao eh possivel remover elementos")
   
elif(posi > n):
    print("[",end=" ")        
    for j in range(len(l)):
        print(l[j],end=" ")
    print("]")
    print("Nao eh possivel remover o elemento")
    
for i in range(len(l)):
    if(i == posi):
        print("[",end=" ")        
        for j in range(len(l)):
            print(l[j],end=" ")
        print("]")
        print("O item",l[i],"serah removido da lista")
        l = l[:(posi)] + l[posi+1:]
        print("[",end=" ")        
        for j in range(len(l)):
            print(l[j],end=" ")
        print("]")
