def calcula_hospedagem(tp, qnt):
    if(tp.upper() == "INDIVIDUAL"):
        if(qnt >= 3):
            valor = 125*qnt*0.85
        else:
            valor = 125*qnt
    elif(tp.upper() == "SU�TE DUPLA"):
        if(qnt >= 3):
            valor = 140*qnt*0.85
        else:
            valor = 140*qnt
    elif(tp.upper() == "SU�TE TRIPLA"):
        if(qnt >= 3):
            valor = 180*qnt*0.85
        else:
            valor = 180*qnt
    return valor

print("%.2f"%calcula_hospedagem(str(input()),int(input())))
