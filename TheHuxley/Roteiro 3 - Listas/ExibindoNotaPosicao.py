n = int(input())
l=[]
soma = 0
cont = 0
if(n > 0):
    for i in range(1, n+1):
        nota = float(input())
        l.append(nota)
        soma +=  nota

    for i in range(len(l)):
        cont += 1
        print("Nota "+str(cont)+": %.1f"%l[i])
    print("Media: %.2f"%(soma/n))
else:
    print("Numero de notas invalido.")
