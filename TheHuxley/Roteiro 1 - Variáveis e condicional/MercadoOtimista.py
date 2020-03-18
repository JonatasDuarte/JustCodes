dia = str(input())
preco = float(input())
op = str(input())
nome = str(input())
precon = float(0)

if(dia == "seg" or dia == "ter" or dia == "qua"):
    if(op == "ouro"):
        precon = preco/2
        print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)
    else:
        precon = 2*preco
        print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)
        
elif(dia == "qui" or dia == "sex"):
    if(10 <= preco <= 100):
        precon = preco/3
        print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)
    else:
        precon = 2*preco
        print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)
        
elif(dia == "sab"):
    if(op == "prata"):
        precon = 3*preco
        print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)
    else:
        precon = 2*preco
        print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)

else:
    precon = 2*preco
    print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)
        
        
