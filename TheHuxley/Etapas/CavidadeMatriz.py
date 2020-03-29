n = int(input())
m = int(input())
matrix=[]
res=""
pos=[]

#Se quadrada
if(m == n):
    for k in range(m):
        linha = []
        for l in range(n):
            num = int(input())
            linha.append(num)
        matrix.append(linha)
    
    menor = int(matrix[0][0])
    for i in range(m):
        for j in range(n):
            if(i == 0 and j == 0):
                cont = 0
            else:
                if(menor>=int(matrix[i][j])):
                    menor = int(matrix[i][j])
                    res += "("+str(i)+", "+str(j)+")"+",  "
                    res = res[:-1]
    print("["+res[:-2]+"]") 