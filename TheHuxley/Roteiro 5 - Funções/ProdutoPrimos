def produtos_primos():
    cont = 0
    soma = 1
    num = input().split() 
    for i in range(len(num)):
        if(int(num[i]) != 1):
            if(int(num[i]) == 2 or int(num[i])%2!=0):
                cont +=1
                soma = soma*int(num[i])

    if(cont == 4):
        return soma
    else:
        return "SEM PRODUTO"

print(produtos_primos())