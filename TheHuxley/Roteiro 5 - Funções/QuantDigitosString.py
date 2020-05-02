def contar_inteiros():
    pa = input()
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    cont = 0
    for i in range(len(pa)):
        if(pa[i] in num):
            cont += 1
    return cont

print(contar_inteiros())