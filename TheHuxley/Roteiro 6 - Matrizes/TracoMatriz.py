matrix = []
va = []
soma =0
n = int(input())
for i in range(n):
    linha = input().split()
    matrix.append(linha)
    va.append(float(matrix[i][i]))
    soma += float(matrix[i][i])
if n > 0:        
    print("tr(A) = ", end='')
    for i in range(len(va)):
        print("(",end='')
        print("%.2f"%float(va[i]), end='')
        print(")",end='')
        if(va[i] == va[-1]): 
            print(" = %.2f"%soma)
        else:
            print(" + ", end='')
else:
    print("tr(A) = 0.00")
    
