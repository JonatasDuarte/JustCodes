def raiz(k, x, cont, res):
    if(int(k) == 1):
        return x
    elif(cont == int(k)):
        return res
    else:
        res += 9
        cont +=1
        return raiz(k, x, cont, res)

n = int(input())
for i in range(n):
    k, x = input().split()
    res = int(x)
    cont=1
    print(raiz(k, x, cont,res))
