quant = int(input())
while (quant != 0):
    if(quant == 1):
        print("0")
    elif(quant > 1):
        fibInicial = 0
        fibSecundario = 1
        print('{} {}'.format(fibInicial,fibSecundario),end='')
        cont = 3
        while(cont <= quant):
            fibFinal = fibInicial + fibSecundario
            print(' {}'.format(fibFinal),end='')
            fibInicial = fibSecundario
            fibSecundario = fibFinal
            cont += 1
        print("")
    quant = int(input())