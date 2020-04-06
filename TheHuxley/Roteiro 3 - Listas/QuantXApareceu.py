lista = []
cont = 0

for i in range(1, 11):
    n = int(input())
    lista.append(n)
    
x = int(input())

for j in range(len(lista)):
    if(lista[j] == x):
        cont += 1

print(cont)
