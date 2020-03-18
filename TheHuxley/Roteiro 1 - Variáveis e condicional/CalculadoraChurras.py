carne = str(input())

conta = 0
pa = 0
pc = 0

if(carne != "C" and carne != "BF" and carne != "BS"):
    print("Op��o inv�lida.")

elif(carne == "C"):
    alho = str(input())
    bebia = str(input())
    bebic = str(input())
    cri = int(input())
    adu = int(input())
    if(bebia == "S" and bebic == "S"):
        conta += (adu*2)*8
        conta += cri*3
    elif(bebia == "S" and bebic == "N"):
        conta += (adu*2)*8
    elif(bebia == "N" and bebic == "S"):
        conta += cri*3
        
    pa += (adu*0.2)*32
    pa += (adu*0.1)*18
    pa += (adu*0.1)*15
    pc += (cri*0.2)*32
    conta += pa+pc
        
    if(alho == "N"):
        print("R$:","%.2f" % (0.98*conta))
    else:
        print("R$:","%.2f" % conta)

elif(carne == "BF"):
    alho = str(input())
    bebia = str(input())
    bebic = str(input())
    cri = int(input())
    adu = int(input())
    if(bebia == "S" and bebic == "S"):
        conta += (adu*2)*8
        conta += (cri*0.5)*6
    elif(bebia == "S" and bebic == "N"):
        conta += (adu*2)*8
    elif(bebia == "N" and bebic == "S"):
        conta += (cri*0.5)*6

    pa += adu*0.25*32
    pa += adu*0.15*18
    pc += cri*0.2*32
    conta += pa+pc

    
    if(alho == "N"):
        print("R$:","%.2f" % (0.98*conta))
    else:
        print("R$:","%.2f" % conta)
    
elif(carne == "BS"):
    alho = str(input())
    bebia = str(input())
    bebic = str(input())
    cri = int(input())
    adu = int(input())
    if(bebia == "S" and bebic == "S"):
        conta += (adu*2)*8
        conta += (cri*0.5)*6
    elif(bebia == "S" and bebic == "N"):
        conta += (adu*2)*8
    elif(bebia == "N" and bebic == "S"):
        conta += (cri*0.5)*6
        
    
    pa += adu*0.25*32
    pa += adu*0.15*15
    pc += cri*0.2*32
    conta += pc+pa
    
    if(alho == "N"):
        print("R$:","%.2f" % (0.98*conta))
    else:
        print("R$:","%.2f" % conta)
    
