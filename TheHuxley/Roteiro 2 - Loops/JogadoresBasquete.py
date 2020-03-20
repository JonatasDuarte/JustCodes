nome = ""
nomemax = ""
nomemin = ""
cont = 0
qnt = 0
total = 0
maior = 0
menor = 1000000

while(nome != 'sair'):
    nome = str(input())
    qnt += 1
    if(nome == "sair"):
        break
    else:
        pont = int(input())
        cont += 1
        total += pont
        if(menor >= pont):
            menor = pont
            nomemin = nome

        if(maior <= pont):
            maior = pont
            nomemax = nome

if(qnt <= 1 and nome == "sair"):
    print("Nenhum jogador foi registrado.")
else:
    print(nomemin)
    print(nomemax)
    print("%.2f"%(total/cont))
