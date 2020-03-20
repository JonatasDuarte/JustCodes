carros = 0
novo = 0
rapido = 0
total = 0
cont = 0
res = ""
qnt = 0

while(res != "n" or res != "N"):
    res = str(input())
    qnt += 1
    if(res == "n" or res == "N"):
        break
    else:
        ano = int(input())
        vel = float(input())
        total += vel
        cont += 1

        if(novo < ano):
            novo = ano

        if(rapido < vel):
            rapido = vel
if(qnt == 1):
    if(res=="n" or res=="N"):
        print("zero")

else:
    print("%.2f"%rapido)
    print(novo)
    print("%.2f"%(total/cont))
