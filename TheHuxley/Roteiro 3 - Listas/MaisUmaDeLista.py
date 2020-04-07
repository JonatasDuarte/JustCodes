n = int(input())
l = []
s = 0
if(n < 0):
    print("O valor informado para N foi negativo")
elif(n == 0):
    print("Lista vazia - O valor de S eh zero")
else:
    for i in range(n):
        l.append(int(input()))
        
    if(n%2 == 0):
        for i in range(len(l)):

            s += ((l[i]-(l[-(i+1)]))**2)
    else:
        l = l[:(n//2)] + [0] + l[n//2:]
        for i in range(len(l)):
            s += ((l[i]-(l[-(i+1)]))**2)

    print("S = %.0f"%(s/2))
