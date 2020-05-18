
def quadrado(l):
    if(l<0):
        qua = -1
    else:
        qua = l*l
    return qua
def retangulo(base, alt):
    if(base < 0 or alt < 0):
        ret = -1
    else:
        ret = base*alt
    return ret
def circulo(r):
    if(r < 0):
        cir = -1
    else:
        cir = 3.14*(r*r)
    return cir

def figuras():
    tipo = ""
    qnt = 0.00
    cont = 0
    mc = -100
    mq = -100
    mr = -100
    fig = []
    while(tipo != "sair"):
        tipo = str(input())
        if(tipo == "sair"):
            break
        if(tipo == "c"):
            cir = circulo(int(input()))
            if(mc < cir):
                mc = cir
            qnt += 1
        elif(tipo == "q"):
            qua = quadrado(int(input()))
            if(mq < qua):
                mq = qua
        elif(tipo == "r"):
            ret = retangulo(int(input()), int(input()))
            if(mr < ret):
                mr = ret
        cont += 1
    pc = (qnt/cont)*100
    fig.append(mc)
    fig.append(mr)
    fig.append(mq)
    fig.append(cont)
    fig.append(pc)
    return fig
fig= figuras()
print("Maior circulo: %.2f"%float(fig[0]))
print("Maior retangulo: %.2f"%float(fig[1]))
print("Maior quadrado: %.2f"%float(fig[2]))
print("Quantidade de figuras",int(fig[3]))
print("Percentual de circulos: %.2f"%float(fig[4]))
