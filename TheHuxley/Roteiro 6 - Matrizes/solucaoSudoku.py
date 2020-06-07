n = int(input())
nun = ['1','2','3','4','5','6','7','8','9']
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i  in range(n):
    mat = []
    nn = 0
    nm = 0
    cont = []
    cont1 = []
    soma = 0
    for co in range(9):
        linha = input().split()
        for j in range(len(linha)):
            soma += int(linha[j])
            
        mat.append(linha)
    
    for k in range(9):
        for h in range(9):
            cont.append(mat[k][h])
        cont = sorted(cont)
        if(cont == nun):
            nn = 0
        else:
            nn= 1
            break
        cont = []
            
    for h in range(9):
        for k in range(9):
            cont1.append(mat[k][h])
        cont1 = sorted(cont1)
        if(cont1 == nun):
            nm=0
        else:
            nm=1
            break
        cont1 = []
           
    if(soma == 405 and (nn!=1 and nm!=1)):
        print("Instancia", i+1)
        print("SIM")
        print()
    else:
        print("Instancia", i+1)
        print("NAO")
        print()

