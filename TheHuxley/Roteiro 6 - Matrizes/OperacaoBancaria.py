op = input().split()
cont=0
ced=0
deb=0
matrix =[]
while int(op[0]) != -1 and cont<=100 :
    cont +=1
    matrix.append(op)
    op = input().split()

for i in range(cont):
    if(int(matrix[i][0]) == 1):
        ced += float(matrix[i][1])
    elif(int(matrix[i][0]) == 0):
        deb += float(matrix[i][1])    
print("Creditos: R$ %.2f"%ced)
print("Debitos: R$ %.2f"%deb)
print("Saldo: R$ %.2f"%(ced-deb))
