k = int(input())
while(k!=0):
    matrix = [[0 for v in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            num = int(input())
            matrix[j][i] = num
    res = ""
    for i in range(4):
        for j in range(4):
            if (i==j):
                res += str(matrix[i][j]*k)+" "
            else:
                res += str(matrix[i][j])+" "
        res = res+"\n"
    print(res[:-1])
    k = int(input())