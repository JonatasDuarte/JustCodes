res = "S"
cont = 0
contv = 0
gastc = 0
gastv = 0
gast = 0
mc = 0
mj = 10000

while(res == "S"):
    ida = int(input())
    gasto = float(input())
    pag = str(input())
    res = str(input())
    cont += 1
    gast += gasto
    
    if(pag == "C"):
        gastc += gasto

    elif(pag == "V"):
        gastv += gasto
        contv += 1
        
    if(mj >= ida):
        mj = ida

    if(mc < gasto):
        mc = gasto

print(cont)

if(gastv == 0):
    print(0)
else:
    print("%.2f"% (gastv))
    
if(gastc == 0):
    print(0)
else:
    print("%.2f"% (gastc))
    
if(cont > 1):
    print(mj)
else:
    print(ida)

if(mc == 0):
    print(0)
else:
    print("%.2f"% (mc))
    
if(gastv >0 and contv>0):
    print("%.2f"% (gastv/contv))
else:
    print(0)

    
