def soma_sucessiva(n1, n2):
    soma=0
    for i in range(abs(n1)):
        soma+=n2
    if(n1<0 and n2<0):
        return abs(soma)
    elif(n1<0):
        return soma-(2*soma)
    else:
        return soma

print(soma_sucessiva(int(input()), int(input())))