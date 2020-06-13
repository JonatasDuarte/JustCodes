n = int(input())
matrix=[]
con=[]
mi=[]
for i in range(n):
    matrix.append(input().split())
mat= "" 
for i in range(n):
    for j in range(n):
        if(int(matrix[j][i]) < 0):
            m = int(matrix[j][i])*2
            mat += str(m) + " "
        else:
            h = int(matrix[j][i])
            mat += str(h) + " "
    print()
    mi.append(con)
    con=[]
    mat = mat[:-1] + "\n"    
print(mat)
